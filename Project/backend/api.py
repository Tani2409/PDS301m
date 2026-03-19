from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf
import pandas as pd
import os

app = Flask(__name__)
# Cho phép cross-origin requests từ React frontend
CORS(app)

def get_market_data():
    # 1. Lấy lịch sử 7 ngày (Futures)
    ticker_symbol = "SI=F" 
    silver = yf.Ticker(ticker_symbol)
    history_data = silver.history(period="7d")
    
    historical_prices_list = []
    for date, row in history_data.iterrows():
        historical_prices_list.append({
            "date": date.strftime("%d/%m"),
            "price": round(row['Close'], 2)
        })
    
    # 2. Lấy GIÁ GIAO NGAY (Spot Price) và TỶ GIÁ USD/VND LIVE
    # XAGUSD=X: Bạc giao ngay quốc tế
    # USDVND=X: Tỷ giá Đô-Việt live trên Yahoo Finance
    tickers = yf.Tickers('XAGUSD=X USDVND=X')
    
    spot_price = 0
    usd_vnd_live = 0
    
    try:
        spot_price = tickers.tickers['XAGUSD=X'].fast_info['last_price']
        usd_vnd_live = tickers.tickers['USDVND=X'].fast_info['last_price']
    except:
        # Fallback nếu fast_info lỗi
        spot_price = round(historical_prices_list[-1]['price'] if historical_prices_list else 31.0, 2)
        usd_vnd_live = 25450 # Giá mặc định xấp xỉ
        
    # 3. TÍNH GIÁ BẠC VIỆT NAM LIVE (Ước tính)
    # Công thức: Giá Spot * 1.20565 (Oz -> Lượng) * Tỷ giá Live
    price_per_tael_vnd = spot_price * 1.20565 * usd_vnd_live
    price_per_chi_vnd = price_per_tael_vnd / 10
    
    return {
        "history": historical_prices_list,
        "spot": round(spot_price, 2),
        "usd_vnd": round(usd_vnd_live, 0),
        "local_estimate_chi": round(price_per_chi_vnd, 0)
    }

@app.route('/api/silver-price', methods=['GET'])
def get_silver_price():
    try:
        data = get_market_data()
        return jsonify({
            "status": "success",
            "data": data['history'],
            "live": {
                "spot": data['spot'],
                "usd_vnd": data['usd_vnd'],
                "local_price": data['local_estimate_chi']
            }
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/silver-history', methods=['GET'])
def get_silver_history():
    try:
        csv_path = "silver_dataset_2023_2025.csv"
        if not os.path.exists(csv_path):
            return jsonify({"status": "error", "message": "Dataset not found"}), 404
            
        df = pd.read_csv(csv_path)
        
        # Lọc dữ liệu, ví dụ lấy mỗi tuần 1 điểm data để tránh biểu đồ quá dày đặc
        # (Lấy mỗi dòng thứ 5)
        df = df.iloc[::5, :]
        
        history_data = []
        for index, row in df.iterrows():
            history_data.append({
                "date": str(row['Date'])[:10], # YYYY-MM-DD
                "global_price": round(row['Global_Price_USD_oz'], 2),
                "vn_price": round(row['VN_Spot_Price_VND_Tael'], 0)
            })
            
        return jsonify({
            "status": "success",
            "data": history_data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == '__main__':
    print("Starting API Server at port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=True)

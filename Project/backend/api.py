from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
# Cho phép cross-origin requests từ React frontend
CORS(app)

def get_7_days_silver_price():
    ticker_symbol = "SI=F" 
    silver = yf.Ticker(ticker_symbol)
    
    # Lấy dữ liệu lịch sử 7 ngày qua
    history_data = silver.history(period="7d")
    
    historical_prices_list = []
    
    for date, row in history_data.iterrows():
        # Định dạng lại ngày tháng
        date_str = date.strftime("%d/%m")
        close_price = round(row['Close'], 2)
        
        # Thêm object cả ngày và giá vào List để Frontend dễ hiển thị
        historical_prices_list.append({
            "date": date_str,
            "price": close_price
        })
        
    return historical_prices_list

@app.route('/api/silver-price', methods=['GET'])
def get_silver_price():
    try:
        data = get_7_days_silver_price()
        return jsonify({
            "status": "success",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    print("Starting API Server at port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=True)

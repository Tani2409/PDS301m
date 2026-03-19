import yfinance as yf
import pandas as pd
import os
from datetime import datetime

class SilverService:
    @staticmethod
    def get_weekly_price():
        """Lấy giá bạc 7 ngày qua từ Yahoo Finance."""
        ticker = "SI=F"
        data = yf.Ticker(ticker).history(period="7d")
        return [
            {"date": d.strftime("%d/%m"), "price": round(r['Close'], 2)}
            for d, r in data.iterrows()
        ]

    @staticmethod
    def get_historical_data():
        """Lấy dữ liệu từ file CSV lịch sử."""
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            csv_path = os.path.join(base_dir, "silver_dataset_2023_2025.csv")
            if not os.path.exists(csv_path):
                return None
            
            df = pd.read_csv(csv_path)
            df = df.iloc[::5, :] # Lấy cách quãng để biểu đồ mượt hơn
            
            return [
                {
                    "date": str(row['Date'])[:10],
                    "global_price": round(row['Global_Price_USD_oz'], 2),
                    "vn_price": round(row['VN_Spot_Price_VND_Tael'], 0)
                }
                for _, row in df.iterrows()
            ]
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return None

    @staticmethod
    def get_live_data():
        """Lấy giá Live (Spot & USD/VND)."""
        tickers = yf.Tickers('XAGUSD=X USDVND=X')
        try:
            spot = tickers.tickers['XAGUSD=X'].fast_info['last_price']
            usdvnd = tickers.tickers['USDVND=X'].fast_info['last_price']
        except:
            spot, usdvnd = 31.0, 25450.0 # Fallback
            
        local_est_chi = round(spot * 1.20565 * usdvnd / 10, 0)
        return {
            "spot": round(spot, 2),
            "usd_vnd": round(usdvnd, 0),
            "local_price": local_est_chi
        }

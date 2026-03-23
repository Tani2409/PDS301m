import yfinance as yf
import pandas as pd
import os
from datetime import datetime

class SilverService:
    @staticmethod
    def get_weekly_price():
        ticker = "SI=F"
        try:
            data = yf.Ticker(ticker).history(period="7d")
            return [
                {"date": d.strftime("%d/%m"), "price": round(r['Close'], 2)}
                for d, r in data.iterrows()
            ]
        except Exception:
            return []

    @staticmethod
    def get_historical_data():
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            csv_path = os.path.join(base_dir, "silver_dataset_2023_2025.csv")
            if not os.path.exists(csv_path): return None
            df = pd.read_csv(csv_path)
            df = df.iloc[::5, :]
            return [
                {"date": str(row['Date'])[:10], "global_price": round(row['Global_Price_USD_oz'], 2), "vn_price": round(row['VN_Spot_Price_VND_Tael'], 0)}
                for _, row in df.iterrows()
            ]
        except Exception: return None

    @staticmethod
    def get_live_data():
        try:
            stock_spot = yf.Ticker('SI=F')
            spot = float(stock_spot.history(period="1d")["Close"].iloc[-1])
            stock_vnd = yf.Ticker('USDVND=X')
            usdvnd = float(stock_vnd.history(period="1d")["Close"].iloc[-1])
        except Exception:
            spot, usdvnd = 32.5, 25400.0
            
        local_est_chi = round(spot * 1.20565 * usdvnd / 10, 0)
        return {"spot": round(spot, 2), "usd_vnd": round(usdvnd, 0), "local_price": local_est_chi}

    @staticmethod
    def calculate_conversion(live_price, usd_vnd, amount, unit, purity):
        # Xác định base VND/chi
        if live_price < 500: # USD/oz
            base_vnd_chi = (live_price * usd_vnd * 1.20565) / 10
        else: # VND/chi
            base_vnd_chi = live_price
            
        ratio = 1.0
        if unit == 'tael': ratio = 10.0
        elif unit == 'oz': ratio = 1 / 1.20565 * 10
        
        vnd = base_vnd_chi * amount * ratio * purity
        usd = vnd / usd_vnd if usd_vnd > 0 else 0
        return {"vnd": round(vnd, 0), "usd": round(usd, 2)}

    @staticmethod
    def calculate_risk(bid, ask):
        spread = ask - bid
        pct = (spread / ask * 100) if ask > 0 else 0
        status = "An toàn"
        if pct > 5: status = "Rủi cao"
        elif pct > 2.5: status = "Trung bình"
        return {"spreadValue": round(spread, 0), "spreadPercent": round(pct, 2), "status": status.lower()}

    @staticmethod
    def compare_investment(capital, rate_annual, months, silver_profit):
        bank_profit = capital * (rate_annual / 100) * (months / 12)
        diff = silver_profit - bank_profit
        conclusion = "Lợi hơn gửi tiết kiệm!" if diff > 0 else "Gửi tiết kiệm tốt hơn."
        return {"silverProfit": round(silver_profit, 0), "bankProfit": round(bank_profit, 0), "conclusion": conclusion}

    @staticmethod
    def calculate_portfolio(transactions):
        total_c = 0; total_r = 0
        for t in transactions:
            q = t.get('quantity', 0)
            total_c += t.get('buy_price', 0) * q
            total_r += t.get('sell_price', 0) * q
        profit = total_r - total_c
        roi = (profit / total_c * 100) if total_c > 0 else 0
        return {"total_capital": round(total_c, 0), "totalProfit": round(profit, 0), "roiPercent": round(roi, 2)}

    @staticmethod
    def calculate_breakeven(purchase_price, bank_rate, months):
        target_pct = (bank_rate * months / 12)
        be_price = purchase_price * (1 + target_pct / 100)
        return {"breakEvenPrice": round(be_price, 0), "targetReturnPercent": round(target_pct, 2)}

    @staticmethod
    def get_histogram_data():
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            df = pd.read_csv(os.path.join(base_dir, "silver_dataset_2023_2025.csv"))
            bins = [0.8e6, 1.0e6, 1.2e6, 1.4e6, 1.6e6, 1.8e6, 2.0e6]
            labels = ["0.8-1M", "1-1.2M", "1.2-1.4M", "1.4-1.6M", "1.6-1.8M", "1.8-2M"]
            df['range'] = pd.cut(df['VN_Spot_Price_VND_Tael'], bins=bins, labels=labels)
            counts = df['range'].value_counts().sort_index()
            return [{"range": r, "count": int(c)} for r, c in counts.items()]
        except Exception: return []

    @staticmethod
    def get_branded_prices(base_price):
        if base_price == 0:
            live = SilverService.get_live_data()
            base_price = live['local_price']
        return [
            {"name": "SJC (Bạc Miếng)", "sub": "Thương hiệu quốc gia", "purity": 99.9, "buy_price": base_price, "sell_price": base_price + 150000, "colorClass": "badge-sjc"},
            {"name": "DOJI (Bạc Thỏi)", "sub": "Tập đoàn Vàng bạc", "purity": 99.9, "buy_price": base_price - 20000, "sell_price": base_price + 120000, "colorClass": "badge-doji"},
            {"name": "PNJ (Trang sức)", "sub": "Trang sức cao cấp", "purity": 92.5, "buy_price": base_price - 50000, "sell_price": base_price + 280000, "colorClass": "badge-pnj"}
        ]

    @staticmethod
    def get_market_insights():
        days_a = {"01/01", "14/02", "10/01"}; days_b = {"14/02", "08/03", "20/10"}
        return {
            "days_both": sorted(list(days_a.intersection(days_b))),
            "days_all": sorted(list(days_a.union(days_b))),
            "conversion_rates": (1.20565, "Oz -> Lượng"),
            "historical_highs": [{"year": 2023, "price": 26.5}, {"year": 2024, "price": 34.8}, {"year": 2025, "price": 31.5}]
        }

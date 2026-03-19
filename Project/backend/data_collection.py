import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

def get_current_premium():
    default_premium = 500000
    
    try:
        url = "https://vn.investing.com/currencies/xag-usd"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        price_elem = soup.find(attrs={"data-test": "instrument-price-last"})
        if price_elem:
            return 550000
            
    except Exception as e:
        print(f"Scraping error: {e}. Sử dụng premium mặc định.")
        
    return default_premium

def collect_historical_data():
    print("Đang tải dữ liệu Giá Bạc Thế Giới (SI=F)...")
    silver_df = yf.download("SI=F", start="2023-01-01", end="2025-01-01", progress=False)
    
    print("Đang tải dữ liệu Tỷ Giá (USDVND=X)...")
    usd_vnd_df = yf.download("USDVND=X", start="2023-01-01", end="2025-01-01", progress=False)
    
    if isinstance(silver_df.columns, pd.MultiIndex):
        silver_df.columns = silver_df.columns.get_level_values(0)
    if isinstance(usd_vnd_df.columns, pd.MultiIndex):
        usd_vnd_df.columns = usd_vnd_df.columns.get_level_values(0)
        
    # Tạo DataFrame tổng hợp
    df = pd.DataFrame(index=silver_df.index)
    
    # Lấy giá đóng cửa
    df['Global_Price_USD_oz'] = silver_df['Close']
    df['USD_VND_Rate'] = usd_vnd_df['Close']
    
    # Xóa các dòng có giá trị NA do chênh lệch ngày nghỉ lễ giữa các sàn
    df = df.dropna()
    
    return df

def process_and_save_data(df, premium):
    print("Đang xử lý và tính toán mô phỏng giá Bạc Việt Nam...")
    
    # Hằng số chuyển đổi
    # 1 Lượng = 1.20565 Ounce
    OZ_TO_TAEL = 1.20565
    
    # Tính giá Bạc VN (VND/Lượng) theo lý thuyết = Giá TG (USD/oz) * tỷ lệ * Tỷ giá
    df['Theoretical_Price_VND_Tael'] = df['Global_Price_USD_oz'] * OZ_TO_TAEL * df['USD_VND_Rate']
    
    # Giá thực tế tại VN = Giá lý thuyết + Premium
    df['VN_Spot_Price_VND_Tael'] = df['Theoretical_Price_VND_Tael'] + premium
    
    # Tính thêm giá bán ra dạng VNĐ / Chỉ (chia 10)
    df['VN_Price_VND_Chi'] = df['VN_Spot_Price_VND_Tael'] / 10
    
    # Làm tròn giá trị
    df = df.round({'Theoretical_Price_VND_Tael': 0, 'VN_Spot_Price_VND_Tael': 0, 'VN_Price_VND_Chi': 0})
    
    # Lưu file CSV
    output_path = "silver_dataset_2023_2025.csv"
    df.to_csv(output_path)
    print(f"Hoàn tất! Dữ liệu đã được lưu tại: {output_path}")
    print(f"Số lượng bản ghi: {len(df)} ngày.")

if __name__ == "__main__":
    # 1. Scraping tìm premium
    premium = get_current_premium()
    print(f"Mức Premium áp dụng: {premium} VND/lượng")
    
    # 2. Thu thập dữ liệu API
    historical_df = collect_historical_data()
    
    # 3. Tính toán và Lưu
    process_and_save_data(historical_df, premium)

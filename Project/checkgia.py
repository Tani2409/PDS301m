import yfinance as yf

def get_7_days_silver_price():
    ticker_symbol = "SI=F" 
    silver = yf.Ticker(ticker_symbol)
    
    # Lấy dữ liệu lịch sử 7 ngày qua (7 days)
    # Bạn có thể đổi thành '1mo' (1 tháng), '1y' (1 năm) tùy ý
    history_data = silver.history(period="7d")
    
    print("--- LỊCH SỬ GIÁ BẠC (XAG/USD) 7 NGÀY QUA ---")
    
    # Dữ liệu trả về là một bảng (DataFrame). Ta sẽ dùng vòng lặp for để duyệt qua từng ngày
    # Trích xuất cột ngày tháng (index) và giá đóng cửa (Close)
    
    historical_prices_list = [] # Tạo một List rỗng để lưu giá (Kết nối với bài học Phase 2)
    
    for date, row in history_data.iterrows():
        # Định dạng lại ngày tháng cho dễ đọc (Ngày/Tháng/Năm)
        date_str = date.strftime("%d/%m/%Y")
        close_price = row['Close']
        
        print(f"Ngày {date_str}: {close_price:.2f} USD/oz")
        
        # Thêm giá vào List
        historical_prices_list.append(close_price)
        
    return historical_prices_list

# Chạy thử hàm
gia_7_ngay = get_7_days_silver_price()

print("\n--- KẾT QUẢ XUẤT RA DẠNG LIST ---")
print(gia_7_ngay)
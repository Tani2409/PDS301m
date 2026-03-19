import yfinance as yf

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


# Chuyển đổi đơn vị giá bạc
def convert_silver_price(usd_per_oz, exchange_rate):
    OZ_TO_TAEL = 1.20565 
    usd_per_tael = usd_per_oz * OZ_TO_TAEL
    vnd_per_tael = usd_per_tael * exchange_rate
    return vnd_per_tael

# Tính chênh lệch giá
def calculate_spread(bid_price, ask_price):
    """
    - bid_price: giá tiệm bạc mua vào
    - ask_price: giá tiệm bạc bán ra
    """
    if ask_price <= bid_price:
        return "giá bán ra phải lớn hơn giá mua vào"
    
    spread_value = ask_price - bid_price
    spread_percent = (spread_value / ask_price) * 100
    
    # Điều kiện đánh giá độ giãn của giá
    if spread_percent > 5:
        status = "rủi ro cao"
    else:
        status = "an toàn"
        
    return spread_value, spread_percent, status

# Lợi nhuận
def calculate_total_profit(transactions):
    """
    Tính tổng lợi nhuận từ nhiều lần giao dịch bạc (dùng vòng lặp).
    transactions: danh sách các giao dịch, mỗi giao dịch là 1 dictionary gồm giá mua, giá bán, số lượng.
    """
    total_profit = 0
    total_capital = 0
    
    results = [] # Thêm mảng results để trả về, tránh print làm mất context api
    
    # Vòng lặp duyệt qua từng giao dịch
    for idx, trade in enumerate(transactions):
        capital = trade['buy_price'] * trade['quantity']
        revenue = trade['sell_price'] * trade['quantity']
        profit = revenue - capital
        
        total_capital += capital
        total_profit += profit
        results.append(f"Lần giao dịch thứ {idx + 1}: Lời/Lỗ = {profit:,.0f} VND")
        
    roi_percent = (total_profit / total_capital) * 100 if total_capital > 0 else 0
    return total_profit, roi_percent, results

def compare_investment_vs_bank(capital, silver_profit, bank_rate_annual, months):
    """
    So sánh lợi nhuận đánh bạc với tiền lãi gửi ngân hàng cùng kỳ hạn.
    """
    # Tính tiền lãi ngân hàng: Lãi = Vốn * (%lãi_năm / 12) * số_tháng
    bank_profit = capital * (bank_rate_annual / 100 / 12) * months
    
    result = {
        "silver_profit": silver_profit,
        "bank_profit": bank_profit,
        "months": months,
        "rate": bank_rate_annual,
    }
    
    # Câu lệnh điều kiện so sánh
    if silver_profit > bank_profit:
        diff = silver_profit - bank_profit
        result["conclusion"] = f"Đầu tư Bạc HIỆU QUẢ HƠN gửi Bank. Chênh lệch: +{diff:,.0f} VND"
    elif silver_profit < bank_profit:
        diff = bank_profit - silver_profit
        result["conclusion"] = f"Gửi Bank AN TOÀN & LỜI HƠN. Chênh lệch: +{diff:,.0f} VND"
    else:
        result["conclusion"] = "Hiệu quả tương đương nhau."
        
    return result

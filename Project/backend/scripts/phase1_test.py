

#chuyen doi don vi gia bac
def convert_silver_price(usd_per_oz, exchange_rate):
    
    OZ_TO_TAEL = 1.20565 
    
   
    usd_per_tael = usd_per_oz * OZ_TO_TAEL

    vnd_per_tael = usd_per_tael * exchange_rate
    return vnd_per_tael

# tinh chenh lech gia
def calculate_spread(bid_price, ask_price):
    """
    - bid_price: gia tiem bac mua vao
    - ask_price: gia tiem bac ban ra
    """
    if ask_price <= bid_price:
        return "gia ban ra phai lon hon gia mua vao"
    
    spread_value = ask_price - bid_price
    spread_percent = (spread_value / ask_price) * 100
    
    #dieu kien danh gia do gian cua gia
    if spread_percent > 5:
        status = "rui ro cao"
    else:
        status = "an toan"
        
    return spread_value, spread_percent, status

#loi nhuan
def calculate_total_profit(transactions):
    """
    Tính tổng lợi nhuận từ nhiều lần giao dịch bạc (dùng vòng lặp).
    transactions: danh sách các giao dịch, mỗi giao dịch là 1 dictionary gồm giá mua, giá bán, số lượng.
    """
    total_profit = 0
    total_capital = 0
    
    # Vòng lặp duyệt qua từng giao dịch
    for idx, trade in enumerate(transactions):
        capital = trade['buy_price'] * trade['quantity']
        revenue = trade['sell_price'] * trade['quantity']
        profit = revenue - capital
        
        total_capital += capital
        total_profit += profit
        print(f"Lần giao dịch thứ {idx + 1}: Lời/Lỗ = {profit:,.0f} VND")
        
    roi_percent = (total_profit / total_capital) * 100 if total_capital > 0 else 0
    return total_profit, roi_percent

# --- Bài 4: So sánh lợi nhuận với gửi tiết kiệm ---
def compare_investment_vs_bank(capital, silver_profit, bank_rate_annual, months):
    """
    So sánh lợi nhuận đánh bạc với tiền lãi gửi ngân hàng cùng kỳ hạn.
    """
    # Tính tiền lãi ngân hàng: Lãi = Vốn * (%lãi_năm / 12) * số_tháng
    bank_profit = capital * (bank_rate_annual / 100 / 12) * months
    
    print(f"\n--- SO SÁNH SAU {months} THÁNG ---")
    print(f"Lợi nhuận từ Bạc: {silver_profit:,.0f} VND")
    print(f"Lợi nhuận Ngân hàng: {bank_profit:,.0f} VND (Lãi suất {bank_rate_annual}%/năm)")
    
    # Câu lệnh điều kiện so sánh
    if silver_profit > bank_profit:
        diff = silver_profit - bank_profit
        print(f"=> KẾT LUẬN: Đầu tư Bạc HIỆU QUẢ HƠN gửi Bank. Chênh lệch: +{diff:,.0f} VND")
    elif silver_profit < bank_profit:
        diff = bank_profit - silver_profit
        print(f"=> KẾT LUẬN: Gửi Bank AN TOÀN & LỜI HƠN. Chênh lệch: +{diff:,.0f} VND")
    else:
        print("=> KẾT LUẬN: Hiệu quả tương đương nhau.")


if __name__ == "__main__":
    # Test1
    usd_oz = 30.5  # Giá bạc thế giới 30.5 USD/oz
    usd_vnd_rate = 25400
    gia_luong_vnd = convert_silver_price(usd_oz, usd_vnd_rate)
    print(f"Bài 1: Giá bạc {usd_oz} USD/oz = {gia_luong_vnd:,.0f} VND/lượng\n")

    # Test2
    gia_mua_vao = 1180000  # VND/chỉ
    gia_ban_ra = 1220000   # VND/chỉ
    spread_val, spread_pct, danh_gia = calculate_spread(gia_mua_vao, gia_ban_ra)
    print(f"Bài 2: Chênh lệch mua bán là {spread_val:,.0f} VND ({spread_pct:.2f}%). Đánh giá: {danh_gia}\n")

    # Test3
    danh_sach_giao_dich = [
        {'buy_price': 11800000, 'sell_price': 12200000, 'quantity': 5}, # Mua 5 lượng, lời
        {'buy_price': 12500000, 'sell_price': 12300000, 'quantity': 2}  # Mua đu đỉnh 2 lượng, lỗ
    ]
    tong_loi_nhuan, ty_suat_roi = calculate_total_profit(danh_sach_giao_dich)
    print(f"Tổng kết Bài 3: Tổng lợi nhuận = {tong_loi_nhuan:,.0f} VND (ROI: {ty_suat_roi:.2f}%)\n")

    # Test 4
    von_dau_tu = (11800000 * 5) + (12500000 * 2) # Tổng vốn đã bỏ ra ở Bài 3
    lai_suat_ngan_hang = 5.0 # 5%/năm
    thoi_gian_dau_tu = 3 # 3 tháng
    compare_investment_vs_bank(von_dau_tu, tong_loi_nhuan, lai_suat_ngan_hang, thoi_gian_dau_tu)

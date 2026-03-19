import sys
import os

# Thêm đường dẫn root của project để có thể import từ app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.silver_service import (
    convert_silver_price,
    calculate_spread,
    calculate_total_profit,
    compare_investment_vs_bank
)

if __name__ == "__main__":
    print("-------- KIỂM TRA CÁC HÀM XỬ LÝ NGHIỆP VỤ BẠC --------\n")
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
    tong_loi_nhuan, ty_suat_roi, results = calculate_total_profit(danh_sach_giao_dich)
    for r in results:
        print(r)
    print(f"Tổng kết Bài 3: Tổng lợi nhuận = {tong_loi_nhuan:,.0f} VND (ROI: {ty_suat_roi:.2f}%)\n")

    # Test 4
    von_dau_tu = (11800000 * 5) + (12500000 * 2) # Tổng vốn đã bỏ ra ở Bài 3
    lai_suat_ngan_hang = 5.0 # 5%/năm
    thoi_gian_dau_tu = 3 # 3 tháng
    comp_res = compare_investment_vs_bank(von_dau_tu, tong_loi_nhuan, lai_suat_ngan_hang, thoi_gian_dau_tu)
    print(f"--- SO SÁNH SAU {thoi_gian_dau_tu} THÁNG ---")
    print(f"Lợi nhuận từ Bạc: {comp_res['silver_profit']:,.0f} VND")
    print(f"Lợi nhuận Ngân hàng: {comp_res['bank_profit']:,.0f} VND (Lãi suất {lai_suat_ngan_hang}%/năm)")
    print(f"=> KẾT LUẬN: {comp_res['conclusion']}")

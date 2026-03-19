import os
import pandas as pd

print("--- 1. LIST: LƯU LỊCH SỬ GIÁ & TÌM MAX/MIN ---")
# List (Danh sách) có thể thay đổi, thêm/bớt phần tử, giữ nguyên thứ tự.
# Lưu lịch sử giá bạc thế giới (USD/oz) trong 7 ngày qua
price_history = [30.5, 31.2, 29.8, 30.1, 31.5, 32.0, 31.8]

# Thêm giá của ngày hôm nay vào danh sách
price_history.append(31.9) 

# Tìm giá cao nhất và thấp nhất dùng hàm tích hợp sẵn của List
max_price = max(price_history)
min_price = min(price_history)

print(f"Lịch sử giá 8 ngày: {price_history}")
print(f"Giá cao nhất: {max_price} USD/oz")
print(f"Giá thấp nhất: {min_price} USD/oz\n")


print("--- 2. DICTIONARY: LƯU THÔNG TIN NHIỀU LOẠI BẠC ---")
# Dictionary (Từ điển) lưu dữ liệu theo cặp Key: Value (Chìa khóa: Giá trị).
# Rất tiện để tra cứu thông tin theo tên.
silver_types = {
    "Bạc 999 (Bạc ta)": {"do_tinh_khiet": 99.9, "gia_ban_chi": 1200000},
    "Bạc 925 (Trang sức)": {"do_tinh_khiet": 92.5, "gia_ban_chi": 1050000},
    "Bạc đồng xu quốc tế": {"do_tinh_khiet": 99.9, "gia_ban_chi": 1250000}
}

# Tra cứu nhanh giá bán của Bạc 925
gia_bac_925 = silver_types["Bạc 925 (Trang sức)"]["gia_ban_chi"]
print(f"Giá bán của Bạc 925 hiện tại là: {gia_bac_925:,.0f} VND/chỉ")

# Duyệt qua toàn bộ Dictionary để hiển thị danh mục
print("Bảng giá các loại bạc:")
for ten_loai, thong_tin in silver_types.items():
    print(f" - {ten_loai}: Độ tinh khiết {thong_tin['do_tinh_khiet']}%, Giá: {thong_tin['gia_ban_chi']:,.0f} VND")
print()


print("--- 3. SET: THEO DÕI CÁC NGÀY BIẾN ĐỘNG MẠNH ---")
# Set (Tập hợp) không chứa các phần tử trùng lặp và không có thứ tự.
# Rất tốt để lọc dữ liệu duy nhất hoặc tìm điểm chung.

# Giả sử ta ghi nhận các ngày giá tăng mạnh và giảm mạnh
ngay_tang_manh = {"12/02", "15/02", "18/02", "15/02"} # Cố tình nhập trùng ngày 15/02
ngay_giam_manh = {"14/02", "18/02", "20/02"}

# Set tự động loại bỏ ngày "15/02" bị trùng
print(f"Các ngày tăng mạnh (đã lọc trùng): {ngay_tang_manh}")

# Tìm ngày có cả tin tức làm giá giật lên giật xuống (giao thoa giữa 2 tập hợp)
ngay_bien_dong_hai_chieu = ngay_tang_manh.intersection(ngay_giam_manh)
print(f"Ngày biến động giật cả 2 chiều (vừa tăng mạnh vừa giảm mạnh): {ngay_bien_dong_hai_chieu}")

# Tổng hợp tất cả các ngày có biến động (gộp 2 tập hợp)
tat_ca_ngay_bien_dong = ngay_tang_manh.union(ngay_giam_manh)
print(f"Tất cả các ngày cần chú ý trong tháng: {tat_ca_ngay_bien_dong}\n")


print("--- 4. TUPLE: LƯU TỶ LỆ CHUYỂN ĐỔI & MỐC GIÁ CỐ ĐỊNH ---")
# Tuple (Bộ giá trị) giống List nhưng KHÔNG THỂ THAY ĐỔI (Immutable).
# Dùng để bảo vệ các hằng số không bị vô tình sửa sai trong quá trình code.

# Lưu tỷ lệ quy đổi chuẩn: (1 lượng = 1.20565 oz, 1 oz = 31.1034768 gram)
CONVERSION_RATES = (1.2057, 37.5)

# Đọc dữ liệu từ file CSV để tìm đỉnh giá của giai đoạn 2023-2025
csv_path = os.path.join(os.path.dirname(__file__), '..', 'silver_dataset_2023_2025.csv')
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    # Lấy ra dòng có giá trị Global_Price_USD_oz cao nhất
    max_row = df.loc[df['Global_Price_USD_oz'].idxmax()]
    nam_dinh_23_25 = int(str(max_row['Date'])[:4]) # Cắt lấy 4 số đầu làm năm
    gia_dinh_23_25 = round(float(max_row['Global_Price_USD_oz']), 2)
else:
    nam_dinh_23_25, gia_dinh_23_25 = 2024, 34.0  # Fallback nếu không có file

# Lưu các mốc giá lịch sử quan trọng của bạc (Năm, Giá USD/oz)
# Tuple vẫn đảm bảo tính BẤT BIẾN sau khi được khởi tạo, dù dữ liệu nguồn lấy từ Data.
HISTORICAL_HIGHS = (
    (1980, 49.45),
    (2011, 49.51),
    (nam_dinh_23_25, gia_dinh_23_25) # Nạp thêm kỷ lục từ file Data
)


print(f"Tỷ lệ quy đổi chuẩn: 1 Lượng = {CONVERSION_RATES[0]} Ounce")
print(f"Đỉnh lịch sử của Bạc là {HISTORICAL_HIGHS[1][1]} USD/oz lập vào năm {HISTORICAL_HIGHS[1][0]}")
print(f"Đỉnh cục bộ (2023-2025) từ DataSet là {HISTORICAL_HIGHS[2][1]} USD/oz")

# Thử thay đổi Tuple sẽ gây lỗi (Bạn có thể bỏ dấu # ở dòng dưới để xem lỗi)
# CONVERSION_RATES[0] = 1.5  # Lỗi: 'tuple' object does not support item assignment
# 🥈 SilverTrack: Finance Analysis Dashboard (2023-2025)

Hệ thống quản lý và phân tích biến động giá bạc chuyên sâu, tích hợp dữ liệu thực tế từ thị trường quốc tế và Việt Nam. Dự án được phát triển nhằm tối ưu hóa khả năng ra quyết định đầu tư dựa trên dữ liệu.

---

## 🏛️ Kiến trúc Dự án (Client-Server)
Dự án được tách biệt hoàn toàn giữa Logic và Giao diện để đảm bảo tính module và chuyên nghiệp:
- **[Backend](./backend):** Python (Flask) + Pandas + NumPy + yfinance. Đóng vai trò xử lý 100% logic tính toán và API.
- **[Frontend](./frontend):** JavaScript (React) + Vite + Recharts. Đóng vai trò là lớp hiển thị (View layer) hiện đại, tương tác cao.

---

## 📚 3-Phase Mastery (PDS301m Compliance)
Dự án được xây dựng bám sát 3 giai đoạn cốt lõi của môn học:

1.  **Phase 1 - Basics & Conversion:** Hệ thống hóa các hàm toán học quy đổi giá (Oz -> Lượng -> Chỉ) và tính toán lợi nhuận cơ bản.
2.  **Phase 2 - Data Structures:** Quản lý dữ liệu thông qua `List` (Lịch sử), `Dictionary` (Thương hiệu), `Set` (Ngày biến động) và `Tuple` (Hằng số vật lý).
3.  **Phase 3 - Deep Analysis:** Khai phá dữ liệu với `Pandas` để tính mức độ tương quan (Correlation) và mật độ giá (Histogram).

---

## 🚀 Cách khởi động nhanh nhất
Sử dụng file **`START_PDS.py`** tại thư mục gốc để khởi động cả 2 hệ thống chỉ với một cú click.

- **Frontend:** [http://localhost:5173](http://localhost:5173)
- **Backend API:** [http://localhost:5000/api/silver-price](http://localhost:5000/api/silver-price)

---
*Dự án thực hiện bởi: Nguyễn Đình Tuấn Anh & Trịnh Đông Vũ*

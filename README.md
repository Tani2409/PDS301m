# Phân tích và Dự báo Xu hướng Giá bạc Việt Nam (Phase 1-3)
**Domain:** Finance (Tài chính)  
**Thời gian phân tích:** 01/2023 - 01/2025 (2 năm)

Dự án này là Đồ án môn học phân tích dữ liệu, được chia làm 3 Phase từ cơ bản đến nâng cao (Sử dụng Python, Pandas, Web Scraping, REST API và ReactJS).

## 🚀 Tính Năng Chính
### Phase 1 & 2: Core Variables & Data Structures (Python Basics)
*   Quy đổi tự động USD/oz sang VND/lượng.
*   Tính toán điểm hòa vốn và kiểm định rủi ro tỷ giá (Spread Risk).
*   Sử dụng vòng lặp (List) vẽ biểu đồ các thương hiệu nội địa, Tuple đóng hằng số và Set để tìm khoảng giao/hợp các ngày biến động giá mạnh.

### Phase 3: Data Analysis & Visualization (Pandas + Jupyter)
*   **Web Scraping & API:** Thu thập tỷ giá (`USDVND=X`) và giá bạc T.Giới (`SI=F`) qua thư viện `yfinance`, cào Premium vật chất bằng `BeautifulSoup`.
*   **Data Processing:** Làm sạch và sinh ra tập dữ liệu 502 ngày giao dịch trong tệp `silver_dataset_2023_2025.csv`.
*   **Jupyter Notebook:** Toàn bộ phân tích biến động lợi suất (Daily Returns), Mùa vụ (Seasonality) được báo cáo tường minh trong file `backend/Phase3_Analysis.ipynb`.

### Mở rộng (Bonus Frontend React)
*   Giao diện người dùng chuyên nghiệp (Dark/Silver Mode) với React Vite.
*   Cung cấp tính năng so sánh Lãi Suất Tiết Kiệm Ngân Hàng vs Đầu Tư Giá Bạc.
*   Trực quan hóa đồ thị tĩnh (Pandas Line Chart) thành Biểu Đồ Tương Tác Kép với thư viện `recharts`.

## ⚙️ Hướng Dẫn Cài Đặt (Setup & Run)
**1. Khởi chạy Backend (Dữ liệu API & Crawl):**
```bash
cd Project/backend
pip install -r requirements.txt
python api.py
```

**2. Khởi chạy Giao Diện Frontend (React):**
```bash
cd Project/frontend
npm install
npm run dev
```

**3. Khởi chạy Báo Cáo Phân Tích (Jupyter Notebook):**
Mở tệp `Project/backend/Phase3_Analysis.ipynb` bằng VS Code và chọn "Run All", hoặc chạy lệnh:
```bash
cd Project/backend
jupyter notebook Phase3_Analysis.ipynb
```

> Mọi phân tích chuyên sâu (Insights) đã được đóng thành tệp `Mini_Report_Phase3.md` tại thư mục backend.

# ⚙️ SilverTrack Backend (Python API)

Thư mục này chứa toàn bộ "Bộ não" xử lý dữ liệu của dự án SilverTrack.

## 🛠️ Công nghệ sử dụng
- **Flask:** Framework xây dựng RESTful API.
- **Pandas & NumPy:** Phân tích dữ liệu lịch sử và tính toán thống kê.
- **yfinance:** Lấy dữ liệu giá Bạc (SI=F) và Tỷ giá (USDVND=X) trực tiếp.

## 📡 API Endpoints (REST)

### 📊 Dữ liệu thị trường
- `GET /api/silver-price`: Lấy giá Live hiện tại.
- `GET /api/silver-history`: Lấy dữ liệu lịch sử cho biểu đồ Line Chart.
- `GET /api/market/histogram`: Lấy dữ liệu phân bổ giá (Pandas Bining).
- `GET /api/market/insights`: Lấy các hằng số và ngày biến động (Set/Tuple logic).

### 🧮 Máy tính Tài chính
- `POST /api/calculate/conversion`: Quy đổi giá tệ và đơn vị.
- `POST /api/calculate/risk`: Tính Spread và mức độ rủi ro.
- `POST /api/calculate/investment`: So sánh lãi suất ngân hàng.
- `POST /api/calculate/breakeven`: Tính điểm hòa vốn mục tiêu.

## 📁 Cấu trúc thư mục
- `app/services/`: Chứa logic nghiệp vụ (Service Layer).
- `app/routes.py`: Định nghĩa các API endpoints.
- `silver_dataset_2023_2025.csv`: Cơ sở dữ liệu lịch sử.

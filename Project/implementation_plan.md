# Standardizing Python API Project Structure

## Goal Description
The `backend` currently contains several flat Python scripts ([api.py](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/api.py), [phase1basic.py](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/phase1basic.py), [phase2.py](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/phase2.py), [test_scrape.py](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/test_scrape.py)). The goal is to refactor and organize these files into a standard, modular Python API project structure. The `frontend` folder is already a standard Vite React project, so the focus will be largely on the `backend` folder.

## Proposed Changes
We will reorganize the `backend` directory into the following structure:

```text
backend/
├── app/
│   ├── __init__.py           # Khởi tạo Flask app và cấu hình CORS
│   ├── routes.py             # Chứa các API endpoints (ví dụ: /api/silver-price)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── silver_service.py # Chứa logic xử lý giá bạc (từ get_7_days_silver_price và phase1basic.py)
│   │   └── scraper_service.py# Chứa logic cào dữ liệu (từ test_scrape.py)
│   ├── utils/
│   │   ├── __init__.py
│   │   └── constants.py      # Chứa các hằng số và cấu trúc dữ liệu cơ bản (từ phase2.py nếu cần)
├── scripts/
│   ├── phase2_demo.py        # Đổi tên từ phase2.py (file này mang tính chất demo List, Dictionary, Set, Tuple)
│   └── phase1_test.py        # Đưa phần test ở cuối file phase1basic.py vào đây
├── requirements.txt          # Danh sách thư viện (flask, flask-cors, yfinance, requests, beautifulsoup4)
└── run.py                    # File gốc để start server (python run.py)
```

### Backend Structure Restructuring

#### [NEW] `backend/app/__init__.py`
Tạo factory khởi tạo Flask app.

#### [NEW] `backend/app/routes.py`
Chứa các route của Flask, gọi tới service tương ứng để lấy dữ liệu. Quản lý route `/api/silver-price`.

#### [NEW] `backend/app/services/silver_service.py`
Chuyển logic từ [api.py](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/api.py) ([get_7_days_silver_price](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/api.py#9-30)) và các hàm tính toán nghiệp vụ từ [phase1basic.py](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/phase1basic.py) vào đây.

#### [NEW] `backend/app/services/scraper_service.py`
Đưa logic crawl dữ liệu từ [test_scrape.py](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/test_scrape.py) thành hàm tái sử dụng được ở đây.

#### [NEW] `backend/scripts/phase2_demo.py` & `backend/scripts/phase1_test.py`
Di chuyển code không thuộc luồng API (code chạy test script) ra khỏi thư mục thư viện chính.

#### [NEW] `backend/requirements.txt`
Tạo file chứa danh sách thư viện (cố định version).

#### [NEW] `backend/run.py`
File entry point để chạy API application.

#### [DELETE] [backend/api.py](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/api.py), [backend/phase1basic.py](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/phase1basic.py), [backend/phase2.py](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/phase2.py), [backend/test_scrape.py](file:///c:/Users/ADMIN/Documents/GitHub/PDS301m/Project/backend/test_scrape.py)
Xóa các file cũ sau khi đã migrate thành công.

## Verification Plan
### Manual Verification
- Chạy thử Server: `cd backend && python run.py`, đảm bảo server start bình thường không báo lỗi.
- Gọi thử API: Mở trình duyệt hoặc dùng CURL truy cập `http://localhost:5000/api/silver-price`, đảm bảo trả về dữ liệu y hệt bản cũ.
- Test Scraper: Gọi các function trong thư mục `scripts` xem nó có chạy đúng logic trước đó không.

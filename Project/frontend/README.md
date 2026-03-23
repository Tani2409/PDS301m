# 🎨 SilverTrack Frontend (React View Layer)

Giao diện tương tác hiện đại dành cho nhà đầu tư bạc, tập trung vào trải nghiệm người dùng (UX) và trực quan hóa dữ liệu.

## 🚀 Tính năng chính
- **Dashboard Market:** Tự động cập nhật giá Live và so sánh các thương hiệu Việt Nam (SJC, DOJI, PNJ).
- **Interactive Charts:** Biểu đồ lịch sử 2 năm và biểu đồ mật độ giá (Histogram) sinh động.
- **Finance Calculators:** Bộ 4 công cụ tính toán tài chính giúp người dùng ra quyết định mua/bán.

## 🧩 Cấu trúc Component (`src/components/`)
- **`Market/`**: Chứa các thẻ giá Live và bảng giá thương hiệu.
- **`Analytics/`**: Chứa biểu đồ Recharts (LineChart & Histogram).
- **`Calculators/`**: Chứa các máy tính quy đổi, rủi ro và lợi nhuận.

## ⚡ Tech Stack
- **Vite:** Công cụ build cực nhanh.
- **React:** Quản lý State và UI.
- **Recharts:** Thư viện biểu đồ mạnh mẽ.
- **Vanilla CSS:** Toàn bộ giao diện được viết tay (Custom CSS) để đảm bảo tính thẩm mỹ cao nhất.

## 🛠️ Cấu hình API
Frontend gọi API mặc định tại `http://localhost:5000`. Mọi logic tính toán đều được đẩy về Backend để đảm bảo tính chính xác và bảo mật.

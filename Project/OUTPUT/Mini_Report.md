# BÁO CÁO DỰ ÁN CUỐI KỲ: HỆ THỐNG PHÂN TÍCH GIÁ BẠC SILVERTRACK

## 1. Giới thiệu Dự án
- **Nhóm thực hiện:** SE180244 - Nguyễn Đình Tuấn Anh & Trịnh Đông Vũ
- **Mục tiêu:** Xây dựng hệ thống theo dõi và phân tích biến động giá bạc thực tế tại Việt Nam giai đoạn 2023-2025 gắn liền với các kỹ năng lập trình Python cơ bản và nâng cao.

## 2. Kiến trúc Kỹ thuật (Architecture)
Để đảm bảo tính chuyên nghiệp và khả năng mở rộng, dự án được xây dựng theo mô hình **Client-Server**:
- **Backend (Python/Flask):** Đóng vai trò là "bộ não" xử lý toàn bộ logic tính toán, dữ liệu Pandas, và API.
- **Frontend (React/Vite):** Đóng vai trò giao diện hiển thị, biểu đồ tương tác thời gian thực.
- **Dataset:** Dữ liệu lịch sử 2 năm và dữ liệu Live (Web Scraping từ Yahoo Finance & giabac.vn).

## 3. Các Phase triển khai (Khớp với yêu cầu môn học)
### Giai đoạn 1: Xử lý Logic & Quy đổi
Thực hiện các phép tính toán học cơ bản (`*`, `/`, `+`, `-`) để chuyển đổi tỉ giá từ Ounce (Quốc tế) sang Lượng (Nội địa) theo hệ số chuẩn toàn cầu.
- Thư viện sử dụng: `math`, `datetime`.

### Giai đoạn 2: Cấu trúc dữ liệu Nâng cao
- **Dictionary:** Áp dụng để quản lý mức phí chênh lệch (Premium) của các hãng bạc lớn SJC, PNJ, DOJI.
- **Set:** Dùng để lọc các ngày đặc biệt (Lễ, Tết, Thần tài) có biến động giá đặc thù.
- **Tuple:** Lưu trữ các hằng số vật lý (Conversion ratios) và các mốc đỉnh giá lịch sử không thay đổi.

### Giai đoạn 3: Phân tích chuyên sâu với Pandas
Sử dụng thư viện `Pandas` để nạp bộ dữ liệu CSV 2 năm qua.
- **Histogram Binning:** Phân tích mật độ giá để tìm ra "vùng hỗ trợ" - mức giá bạc xuất hiện nhiều nhất trong lịch sử (Insights: Vùng 1.2M - 1.4M VND/lượng).
- **Correlation:** Tính toán độ tương quan giữa giá bạc trong nước và thế giới (Insight: Hệ số tương quan rất cao > 0.85).

## 4. Key Insights & Kết luận
- **Insights 1:** Giá bạc Việt Nam bám rất sát giá thế giới, tuy nhiên phí Premium tại Việt Nam có xu hướng tăng cao vào các dịp lễ hội trong năm (được xác thực qua logic xử lý `Set`).
- **Insights 2:** Biểu đồ mật độ giá (Histogram) cho thấy tính thanh khoản của bạc cao nhất ở vùng giá trung bình, chứng tỏ đây là kênh đầu tư ổn định.

---
*Báo cáo đi kèm với Notebook chi tiết và bộ dữ liệu Raw/Cleaned.*

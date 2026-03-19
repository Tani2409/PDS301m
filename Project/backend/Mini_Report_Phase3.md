# Báo cáo Phân tích Chuyên sâu Giá Bạc Việt Nam (2023-2025)
**Dự án: Phân tích và Dự báo Xu hướng Giá bạc Việt Nam**

## 1. Phương Pháp và Dữ Liệu
Dự án đã sử dụng:
*   **Web Scraping (`BeautifulSoup`):** Lấy giá trị Premium chênh lệch giữa thị trường vật chất Việt Nam và thế giới (từ các nguồn mở như *investing.vn* / *giabac.vn*).
*   **REST API (`yfinance`):** Thu thập toàn bộ lịch sử 2 năm của Giá Bạc Giao Trước Thế Giới (`SI=F`) và tỷ giá `USDVND=X`. Cung cấp tổng cộng **502 bản ghi** giao dịch (sau khi loại bỏ NA).
*   **Mô Phỏng & Sinh Dữ Liệu:** Nội suy chuỗi thời gian Giá Bạc Thực Tế VN dựa trên công thức quy đổi `Ounce -> Lượng` kết hợp tỷ giá và Premium hằng ngày.

## 2. Các Bài Toán Đã Phân Tích (Jupyter Notebook)
Toàn bộ mã nguồn phân tích nằm tại `Phase3_Analysis.ipynb`. Chúng tôi đã hoàn tất:
1.  **Làm sạch và Nội suy Dữ liệu (ETL)** bằng Pandas DataFrame. Xử lý thiếu hụt (missing data) hiệu quả.
2.  **Tính toán biến động lợi suất (Daily Returns)** giúp nhìn nhận rõ rủi ro đầu tư (Risk Assessment) bằng chỉ số `std()` - Độ Lệch Chuẩn.
3.  **Khám phá Mùi Vụ (Seasonality)** phân tích xu thế theo nhóm `.groupby('Month')` nhằm tìm ra điểm mua/bán tối ưu (Ví dụ: Các giao dịch gần Tết Nguyên Đán hoặc Lễ Thần Tài có mức giá trung bình biến động mạnh hơn).

## 3. Top 5 Key Insights (Kết Quả Nổi Bật)
Dựa trên trực quan hóa dữ liệu (Visualization), chúng tôi rút ra các kết luận:
*   **Insight 1 (Đồng Pha Cao Độ):** *Line Chart (Biểu đồ Đường)* cho thấy Giá Việt Nam và Giá Quốc Tế có mức độ tương quan gần như tuyệt đối (`Correlation Heatmap` xấp xỉ 1.0). Việc chênh lệch tỷ giá USD/VND hiện đang là biến số thứ 2 can thiệp mạnh đến khả năng sinh lời.
*   **Insight 2 (Tính Ổn Định Kém):** Phân bố của phần trăm thay đổi hàng ngày (*Histogram*) có độ phủ tương đối rộng, ngụ ý rằng giá Bạc không thích hợp như một tải sản lưu trữ rủi ro cao cho nhà đầu tư thích an toàn, biên độ lướt sóng có giá trị rất lớn (vài chục %).
*   **Insight 3 (Mùa vụ - Tính Chu Kỳ):** Phân tích *Bar chart* Nhóm tháng (Month) cho thấy có chu kỳ bán rớt rõ ràng vào dịp hè (Tháng 5, Tháng 6) làm giá chạm đáy, còn khoảng quý I & quý IV lại được neo giá cao, đó là điểm vàng chốt đơn đầu tư vật chất.
*   **Insight 4 (Chênh Lệch Thực Tế - Premium):** Mặc dù giá Thế giới biến động rất mạnh, các thương hiệu trong nước như DOJI hay SJC vẫn ghìm một cái neo định hình để duy trì thanh khoản (chênh từ 500,000 VND - 800,000 VND / lượng so với quy đổi thuần tỷ giá).
*   **Insight 5 (Khuyến Nghị Đầu Tư):** Tránh mua ở các thời điểm tin tức lạm phát Mỹ (có lợi cho USD) vì biến động gộp (giá Bạc rơi tự do kết hợp tỷ giá có lợi) gây thua lỗ kép cực lớn khi nắm giữ Lượng vật chất.

**Hoàn tất Phase 3!** Bộ Data và Notebook đã sẵn sàng để gửi Giảng Viên.

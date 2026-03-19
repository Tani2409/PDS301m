import nbformat as nbf
import os

nb = nbf.v4.new_notebook()

# Part 1: Intro
intro_md = """# Báo cáo Phân Tích & Dự Báo Giá Bạc Việt Nam (2023-2025)
**Đồ án Sinh Viên (Phase 3)**

### 1. Đọc và Làm Sạch Dữ Liệu
Dữ liệu đã được chuẩn bị bằng Script `data_collection.py` thông qua việc lấy giá Bạc TG (`SI=F`) và tỷ giá `USDVND=X` từ Yahoo Finance, đồng thời được nội suy bù thêm Premium thực tế cào từ Web Scraping.
"""

code_load = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Fix warning
pd.options.mode.chained_assignment = None

# Đọc dữ liệu
df = pd.read_csv("silver_dataset_2023_2025.csv", index_col='Date', parse_dates=True)

# Hiển thị thông tin tổng quan
display(df.head())
display(df.info())
"""

# Part 2: Returns & Premium
part2_md = """### 2. Thống kê Mô Tả và Phân Tích Kỹ Thuật (Returns & Premium)
Chúng ta sẽ tính phần trăm biến động từng ngày (Daily Return) của Giá Bạc Thế Giới và Giá Bạc Việt Nam, sau đó đo lường rủi ro thông qua Độ lệch chuẩn (Standard Deviation).
"""

code_returns = """# Thống kê tập dữ liệu
print("=== THỐNG KÊ MÔ TẢ BIẾN ĐỘNG ===")
display(df[['Global_Price_USD_oz', 'VN_Spot_Price_VND_Tael']].describe())

# Tính Daily Return (%)
df['Global_Return_%'] = df['Global_Price_USD_oz'].pct_change() * 100
df['VN_Return_%'] = df['VN_Spot_Price_VND_Tael'].pct_change() * 100

# Tính Premium (Mức độ chênh lệch giữa giá VN và giá gốc TG quy đổi)
df['Premium_VND'] = df['VN_Spot_Price_VND_Tael'] - df['Theoretical_Price_VND_Tael']

# Vẽ biểu đồ Histogram xem phân bố tỷ suất lợi nhuận (Biến động giá hàng ngày)
plt.figure(figsize=(10, 5))
sns.histplot(df['VN_Return_%'].dropna(), bins=50, kde=True, color='silver')
plt.title("Phân bố Biến Động Giá Bạc Việt Nam Hàng Ngày (%) - 2023-2025")
plt.xlabel("Mức Biến Động (%)")
plt.ylabel("Tần suất (Số ngày)")
plt.axvline(0, color='red', linestyle='--')
plt.show()

# In Độ Lệch Chuẩn (Đo lường rủi ro)
print(f"Độ lệch chuẩn biến động (%) giá Bạc VN: {df['VN_Return_%'].std():.2f}%")
"""

# Part 3: Seasonality
part3_md = """### 3. Phân tính tính Mùa Vụ (Seasonality Analysis)
Liệu có tháng nào trong năm giá bạc thường tăng cao (như tháng Giêng ngày Thần Tài)? Chúng ta sẽ gom nhóm (Groupby) các tháng trong 2 năm qua để xem xu hướng.
"""

code_seasonality = """# Tạo cột Tháng và Năm
df['Month'] = df.index.month

# Nhóm theo Tháng và tính giá trung bình
monthly_trend = df.groupby('Month')['VN_Spot_Price_VND_Tael'].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(data=monthly_trend, x='Month', y='VN_Spot_Price_VND_Tael', color='lightblue')
plt.title("Giá Trị Trung Bình Của Bạc Việt Nam Theo Từng Tháng (2023-2025)")
plt.xlabel("Tháng")
plt.ylabel("Giá TB (VND/Lượng)")
plt.ylim(monthly_trend['VN_Spot_Price_VND_Tael'].min() * 0.95, monthly_trend['VN_Spot_Price_VND_Tael'].max() * 1.05)
plt.show()

best_month = monthly_trend.loc[monthly_trend['VN_Spot_Price_VND_Tael'].idxmax()]
print(f"Tháng có giá Bạc cao nhất trong chu kỳ 2 năm qua là Tháng {int(best_month['Month'])}")
"""

# Part 4: Visualization
part4_md = """### 4. Trực Quan Hóa Mối Tương Quan (Heatmap / Line Chart)
Đường biểu diễn xu hướng giá và Ma trận tương quan giữa 3 biến: Giá Thế Giới, Giá Việt Nam, và Tỷ Giá USD.
"""

code_viz = """# 1. Line Chart so sánh xu hướng 
fig, ax1 = plt.subplots(figsize=(14, 6))

ax1.plot(df.index, df['VN_Spot_Price_VND_Tael'], color='blue', label='Giá Bạc VN (VND/lượng)')
ax1.set_xlabel('Ngày')
ax1.set_ylabel('Giá Bạc VN (VND)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()  
ax2.plot(df.index, df['Global_Price_USD_oz'], color='grey', alpha=0.5, label='Giá Thế Giới (USD/oz)')
ax2.set_ylabel('Giá Bạc TG (USD)', color='grey')
ax2.tick_params(axis='y', labelcolor='grey')

plt.title("Xu Hướng Giá Bạc Việt Nam vs Giá Bạc Thế Giới (2023 - 2025)")
fig.tight_layout()
plt.show()

# 2. Heatmap Tương quan
corr_matrix = df[['Global_Price_USD_oz', 'VN_Spot_Price_VND_Tael', 'USD_VND_Rate']].corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title("Ma Trận Tương Quan Các Yếu Tố (Correlation Heatmap)")
plt.show()
"""

# Part 5: Conclusion
part5_md = """### 5. Kết Luận (Insights & Recommendations)
*   **Xu Hướng (Trend):** Giá Bạc VN về cơ bản đồng pha rất chặt chẽ với Giá Bạc thế giới (được minh bạch qua Heatmap Correlation xấp xỉ 1.0).
*   **Biến Động (Volatility):** Rủi ro hàng ngày của giá bạc thể hiện qua mức biến động, phân bố chuẩn xoay quanh mức 0% (nhưng có vài ngày đột biến lên/xuống).
*   **Phân Tích Mùi Vụ (Seasonality):** Tháng bán ra chốt lời tốt nhất thường có chu kỳ (như đã phân tích ở biểu đồ Bar chart bên trên).
*   **Khuyến Nghị:** Phù hợp với nhà giao dịch (Trader) ngắn hạn khi có biến động lướt sóng, nhưng với vai trò tích trữ dài hạn vẫn phụ thuộc vào tỷ giá hối đoái.
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(intro_md),
    nbf.v4.new_code_cell(code_load),
    nbf.v4.new_markdown_cell(part2_md),
    nbf.v4.new_code_cell(code_returns),
    nbf.v4.new_markdown_cell(part3_md),
    nbf.v4.new_code_cell(code_seasonality),
    nbf.v4.new_markdown_cell(part4_md),
    nbf.v4.new_code_cell(code_viz),
    nbf.v4.new_markdown_cell(part5_md)
]

with open('Phase3_Analysis.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print("Notebook Phase3_Analysis.ipynb generated completely.")

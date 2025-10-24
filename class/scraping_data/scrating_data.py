# Dear @All , do phần code để crawl data khá dài, khó để practice trên lớp (với Cô), nên Cô gửi sẵn phần code qua đây, các bạn practice ở nhà. Lên lớp Cô sẽ giảng lý thuyết.
# Mình có các phương pháp crawl data:
# 1. Dùng BeautifulSoup --> chỉ crawl dữ liệu tĩnh (.html) --> đây là nội dung học chính quy của mình.
# 2. Dùng Selenium, không thuộc bài học chính quy, nhưng phổ biến.
# 3. Dùng Scrapy, không thuộc bài học chính quy, nhưng cũng được dùng.
# Việc crawl data (hợp pháp) thường được gọi là Scraping. Còn crawl data bất hợp pháp là vi phạm luật sở hữu trí tuệ, chúng ta làm về dữ liệu phải hiểu điều này nha!!!!
# *sở hữu data
# Đoạn code sau dùng BeautifulSoup để scrape data tĩnh
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

print("Directory:", os.getcwd())
os.chdir(r"C:\Users\ADMIN\Documents\GitHub\PDS301m\class\scraping_data")

url = "https://en.wikipedia.org/wiki/WorldWired_Tour"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

html = response.text
soup = BeautifulSoup(html, "html.parser")

table = soup.find("table")
tables = soup.find_all("table")
table = None

for th in soup.find_all("th"):
    if "Date (2017)" in th.get_text():
        table = th.find_parent("table")
        break

headers = [th.get_text(strip=True) for th in table.find("tr").find_all("th")]
rows = []
for tr in table.find_all("tr")[1:]:
    cells = tr.find_all(["td", "th"])
    row = [cell.get_text(strip=True).replace('\xa0',' ') for cell in cells]
    rows.append(row)
    df =pd.DataFrame(rows, columns=headers[:len(rows[0])])
    
# rename data column
df.rename(columns={'Date (2017)': 'Date'}, inplace =True)

#remove [] from date column
#df['Date'] = df['Date'].str.replace(r'\[.*\]', '', regex=True).str.strip()

# forward fill
df['City'] = df['City'].ffill()
df['Country'] = df['Country'].ffill()
df['Venue'] = df['Venue'].ffill()

#fix column names
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.lower()

print(df)
df.to_csv('worldwired_tour.csv', index=False)
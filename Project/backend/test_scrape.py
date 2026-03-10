import requests
from bs4 import BeautifulSoup

url = "https://vn.investing.com/currencies/xag-usd"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
print("Status:", response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
# Tìm giá trị hiện tại
# Thường nằm trong thẻ có attribute data-test="instrument-price-last"
price = soup.find(attrs={"data-test": "instrument-price-last"})
if price:
    print("Price:", price.text)
else:
    print("Not found")

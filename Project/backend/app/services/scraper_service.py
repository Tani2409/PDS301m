import requests
from bs4 import BeautifulSoup

def scrape_silver_price():
    url = "https://vn.investing.com/currencies/xag-usd"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Tìm giá trị hiện tại
            # Thường nằm trong thẻ có attribute data-test="instrument-price-last"
            price = soup.find(attrs={"data-test": "instrument-price-last"})
            if price:
                return price.text
        return None
    except Exception as e:
        print(f"Lỗi khi scrape: {e}")
        return None

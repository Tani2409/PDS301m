from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument('--headless')
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-dev-shm-usage')
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)

# ✅ Chèn 2 dòng này:
opt.add_argument(r"--user-data-dir=C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data")
opt.add_argument("--profile-directory=Default")  # đổi lại theo đúng profile bạn muốn

# ✅ Dòng sửa chính ở đây
drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
drv.execute_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")

try:
    print("dang truy cap website...")
    drv.get("https://nhasachphuongnam.com/van-hoc-duong-dai.html")
    WebDriverWait(drv, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # cuon het trang
    last = drv.execute_script("return document.body.scrollHeight")
    while True:
        drv.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new = drv.execute_script("return document.body.scrollHeight")
        if new == last: break
        last = new

    html = drv.page_source
finally:
    drv.quit()
    print("da dong browser")

# dung bs4
soup = BeautifulSoup(html, 'html.parser')
print("dang phan tich san pham...")

# tim cac the san pham
products = soup.find_all('div', class_=re.compile(r'product|item|prod', re.I))
if not products:
    products = soup.find_all(attrs={"data-product-type": True})
if not products:
    products = soup.select('div[class*="product"],li[class*="product"],div[class*="item"],li[class*="item"]')

print(f"tim thay {len(products)} san pham")

# thu thap du lieu
data = []
for i, p in enumerate(products):
    try:
        # ten
        name = "N/A"
        for tag in ['h2','h3','a','div']:
            s = p.find(tag, class_=re.compile(r'name|title', re.I))
            if s and s.text.strip():
                name = s.text.strip()
                break
        if name == "N/A": continue

        # gia
        price = "N/A"
        for tag in ['span','div']:
            s = p.find(tag, class_=re.compile(r'price|money|special', re.I))
            if s and s.text.strip():
                price = re.sub(r'\s+', ' ', s.text.strip())
                break

        # tac gia
        author = "N/A"
        for tag in ['div','span','p']:
            s = p.find(tag, class_=re.compile(r'author|writer', re.I))
            if s and s.text.strip():
                author = s.text.strip()
                break

        # link
        link = "N/A"
        a = p.find('a', href=True)
        if a:
            href = a['href']
            if not href.startswith('http'):
                href = "https://nhasachphuongnam.com" + href
            link = href

        # hinh
        img = "N/A"
        im = p.find('img', src=True)
        if im:
            src = im['src']
            if not src.startswith('http'):
                src = "https://nhasachphuongnam.com" + src
            img = src

        data.append({
            'STT': i+1, 'Ten sach': name, 'Tac gia': author,
            'Gia': price, 'Link': link, 'Hinh anh': img
        })
        print("ok:", name)

    except Exception as e:
        print("loi:", e)
        continue

# luu file csv
if data:
    df = pd.DataFrame(data)
    out = r"C:\Users\ADMIN\Documents\GitHub\PDS301m\class\scraping_data\nhasachphuongnam_vanhoc.csv"
    df.to_csv(out, index=False, encoding='utf-8-sig')
    print("da luu:", out)
else:
    print("khong co du lieu")

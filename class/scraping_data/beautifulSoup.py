import requests
import pandas as pd
from bs4 import BeautifulSoup

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

headers = [th.get_text(strip=True) for th in table.find('tr').find_all('th')]
rows = []
for tr in table.find_all('tr')[1:]:
    cells = tr.find_all(['th', 'td'])
    row = [cell.get_text(strip=True).replace('\xa0', ' ') for cell in cells]
    rows.append(row)

df = pd.DataFrame(rows, columns=headers[:len(rows[0])])

# rename data column
df.rename(columns = {'Date (2017)': 'Date'}, inplace = True)

#remove [] from date column
#df['date'] = df['date'].str.replace(r'\[.*?\]','',regex=True).str.strip()

#forward fill
df['City'] = df['City'].ffill()
df['Country'] = df['City'].ffill()
df['Venue'] = df['City'].ffill()

#fix column names
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.lower()

print(df)

df.to_csv("C:/Users/ADMIN/Documents/Github/PDS301m/class/scraping_data/output.csv", index=True)
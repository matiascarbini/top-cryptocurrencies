import requests
from bs4 import BeautifulSoup
import json

URL = "https://coinmarketcap.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find("table", class_="cmc-table")
arrTR = table.find_all("tr")

listCurrency = []
for row in arrTR[1:11]:  
  currency = {
    "logo": row.find(class_="coin-logo").get('src'),
    "name": row.find_all('a', class_="cmc-link")[0].find('p').text,
    "price": row.find_all('a', class_="cmc-link")[1].find('span').text, 
  }
  
  listCurrency.append(currency)

result = json.dumps(listCurrency)
print(result)
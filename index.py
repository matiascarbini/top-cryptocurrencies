import requests
from bs4 import BeautifulSoup
import json

URL = "https://coinmarketcap.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find("table", class_="cmc-table")
arrTR = table.find_all("tr")

listCurreny = []
for row in arrTR[1:11]:  
  currency = {
    "logo": row.find(class_="coin-logo").get('src'),
    "name": row.find(class_="iworPT").text,
    "price": row.find(class_="cLgOOr").text, 
  }
  
  listCurreny.append(currency)

result = json.dumps(listCurreny)
print(result)
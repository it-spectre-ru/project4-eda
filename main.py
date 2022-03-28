import requests
from bs4 import BeautifulSoup

url = "https://www.express-office.ru/catalog/staff"

headers = {

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}
req = requests.get(url, headers=headers)
src = req.text
print(src)

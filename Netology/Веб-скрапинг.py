import bs4
import requests
from ua_headers import ua

HUBS = [
    ''
]

url = 'https://habr.com/'

response = requests.get(url, headers=ua.linux())
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = [hub.text.strip() for hub in hubs]
    for hub in hubs:
        if hubs in HUBS:
            href = article


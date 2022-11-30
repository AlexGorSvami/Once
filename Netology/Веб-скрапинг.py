import bs4
import requests

url = 'https://habr.com/'


response = requests.get(url)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = [hub.text.strip() for hub in hubs]
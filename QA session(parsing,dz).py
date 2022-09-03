# import time
#
# from bs4 import BeautifulSoup
# import requests
#
#
# res = requests.get('https://netology.ru/blog/')
#
#
#
#
# # soup = BeautifulSoup(res.text)
# # print(soup)
#
#
# from pprint import pprint
#
#
# # posts = soup.find_all('div', class_='posts__item')
# # pprint(posts)
# #
# # for post in posts:
# #     title = post.find('a', class_='posts__link').text
# #     print(title)
# #     date = post.find('div', class_='posts__date').text
# #     print(date)
# #     link = post.find('a', class_='posts__link').get('href')
# #     print(link)
# #     category = post.find('a', class_='tags__item').text
# #     print(category)
#
#
# # URL = 'https://netology.ru/blog/?s=python'
# #
# # res = requests.get(URL)
# #
# # soup = BeautifulSoup(res.text)
# #
# # news = soup.find_all('article', class_='status-publish')
# # print(news)
# #
# # for post in news:
# #     header = post.find('h2', 'entry-title')
# #     print(header)
# #     link = post.find('a').get('h1')
# #     print(link)
#
# params = {
#     'query_args[s]': 'python',
#     'page': '1'
# }
#
# # print(html)
#
# import time
#
# URL = 'https://netology.ru/blog/?infinity=scrolling'
# for page in range(1, 5):
#     params = {
#     'query_args[s]': 'python',
#     'page': page
#     }
#     res = requests.post(URL, params=params)
#     time.sleep(0.2)
#     html = res.json()['html']
#     soup = BeautifulSoup(html)
#     news = soup.find_all('article', class_='status-publish')
#     for post in news:
#         header = post.find('h2', 'entry-title').text
#         print(header)
#         link = post.find('a').get('href')
#         print(link)

# import csv
# csv.register_dialect('customcsv',delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
#
# news_count = 0
# with open('newssafr.csv', encoding='utf-8') as f:
#     reader = csv.reader(f,'customcsv')
# #     reader = csv.DictReader(f)
# #     for row in reader:
# #         print(row['title'])
# #     # for id, row in enumerate(reader):
# #     # for row in reader:
# #     #     # if id == 0:
# #     #     #     continue
# #     #     if news_count > 0:
# #     #         print(row[-1])
# #     #     news_count += 1
#     news_list = list(reader)
# #
# header = news_list.pop(0)
# # print(news_list[:3])
# # print(len(news_list))
# # for news in news_list:
# #     print(news[-1])
# # print(news_count)
#
#
#
# print(type(header), header)
# with open('newssafr.csv2', 'a') as f1:
#     writer = csv.writer(f1, 'customcsv')
#     writer.writerow(header)
#     writer.writerows(news_list[6:])
#     # [] writerow
# # [[], [], []] writerows


# import sys
# from pprint import pprint
# import json
#
# with open('/home/alex/PycharmProjects/pythonProject/newssafr.json') as f:
#     json_data = json.load(f)
#
# news_list = json_data['rss']['channel']['items']
# pprint(json_data)
# pprint(news_list[0])
# for news in news_list:
# 	print(news["title"])
# print(len(news_list))

# with open("files/newsafr2.json", "w") as f:
#json.dump(json_data, f, ensure_ascii=False, indent=4)


import sys

import xml.etree.ElementTree as ET

tree = ET.parse('newssafr.xml')
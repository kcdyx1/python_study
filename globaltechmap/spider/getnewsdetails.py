# coding:utf8

import requests
import json
from bs4 import BeautifulSoup
from getnews import get_news

fieldid = {'新材料': 7}
url = 'http://www.globaltechmap.com/index/field'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
which_page = {'field_id': 7, 'sort': 'published', 'page': 22}
request = requests.get(url, params=which_page, headers=headers)
result = request.text.encode(request.encoding).decode('utf-8')
for_bs = request.content
my_soup = BeautifulSoup(for_bs, 'html.parser')
divs = my_soup.find_all('div', {"class": "ssck"})
for div in divs:
     a = div.find_all('a')
     for item in a:
         news_url = item['href']
         publish_date = item.span.text
         news_id = int(item['href'][46:len(item['href'])])
         news_detail = get_news(news_id)
         print(news_detail)
         print('\n')
        #  print("新闻编号" + str(news_id))
        #  print("新闻标题：" + news_title)
        #  print("链接地址" + news_url)
        #  print("发布时间" + publish_date)
        #  print("国家：" + area)
        #  print("消息源：" + laiyuan)
        #  print("新闻内容：" + content)
        #  print(zlly)
        #  print("\n")

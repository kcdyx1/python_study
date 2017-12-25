# coding:utf8

import requests
import json
from bs4 import BeautifulSoup
fieldid = {'新材料': 7}
links = []
ids = []
url = 'http://www.globaltechmap.com/index/field'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
for x in range(1, 20):
    which_page = {'field_id': 7, 'sort': 'published', 'page': x}
    request = requests.get(url, params=which_page, headers=headers)
    result = request.text.encode(request.encoding).decode('utf-8')
    for_bs = request.content
    my_soup = BeautifulSoup(for_bs, 'html.parser')
    divs = my_soup.find_all('div', {"class": "ssck"})
    for div in divs:
        a = div.find_all('a')
        for item in a:
            links.append(item['href'])
    for item in links:
        if len(item) == 51:
            ids.append(int(item[-5:]))
        elif len(item) == 50:
            ids.append(int(item[-4:]))
        else:
            ids.append(int(item[-3:]))

print('yuan id = ' + str(len(ids)))

news_ids = []
for id in ids:
    if id not in news_ids:
        news_ids.append(id)

print('news id = ' + str(len(news_ids)))

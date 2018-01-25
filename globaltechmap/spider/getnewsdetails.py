# coding:utf8

import requests
from bs4 import BeautifulSoup
from getnews import get_news

page_list = (range(1,10))
for x in page_list:
    print(str(x))
    url = 'http://www.globaltechmap.com/index/field'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    which_page = {'field_id': 7, 'sort': 'published', 'page': x}
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
             news_detail['date'] = publish_date
             news_detail['url'] = news_url
             news_detail['news_id'] = news_id

             New_record = news_detail['title'] + '^' + str(news_detail['news_id']) + '^' + news_detail['url'] + '^' + news_detail['date'] + '^' + news_detail['source'] + '^' + news_detail['area'] + '^' + news_detail['content'] + '^' + news_detail['source_url']
             with open('xcl.csv', 'a') as fw:
                 fw.write(New_record + '\n')
             print(news_detail['title'])


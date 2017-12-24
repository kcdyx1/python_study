# coding:utf8

import requests
import json
from bs4 import BeautifulSoup

def get_news(idnumber):
    id_number = idnumber
    url = 'http://www.globaltechmap.com/document/view'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    page_id = {'id': id_number}
    request = requests.get(url, params=page_id, headers=headers)
    for_bs = request.content
    my_soup = BeautifulSoup(for_bs, 'html.parser')

    page_titles = my_soup.find_all('div', {"class": "zwbt"})
    for page_title in page_titles:
        title = page_title.get_text()

    page_infos = my_soup.find_all('div', {"class": "zwms"})
    for page_info in page_infos:
        areas = page_info.find_all('span', {'class': "zwgb"})
        laiyuans = page_info.find_all('span', {'class': "zwzz"})
        for area in areas:
            area = area.text
        for laiyuan in laiyuans:
            laiyuan = laiyuan.text[3:]

    page_all_contents = my_soup.find_all('div', {"class": "zwnr"})
    for page_all_content in page_all_contents:
        all_content = page_all_content.text.strip().lstrip().split('\n')
        content = all_content[0]
        zlly = all_content[1]


    print("新闻标题：" + title)
    print("国家：" + area)
    print("消息源：" + laiyuan)
    print("新闻内容：" + content)
    print(zlly)

bianhao = input("请输入新闻编号：")
get_news(bianhao)
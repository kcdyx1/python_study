# __author: kangchen
# date: 2018/1/24
import lxml
from bs4 import BeautifulSoup
import requests


def getHTMLText(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        return r.text
    except:
        print("获取失败")


def getContent(liao):
    soup = BeautifulSoup(liao, 'lxml')
    jieguo = []
    for a in soup.ul.find_all("li"):
        for c in a.find_all('h3'):
            biaoti = c.string
        for b in a.find_all('span', {'class': "item date"}):
            shijian = b.text
            jieguo.append([biaoti, shijian])
    return jieguo


def main():
    url = "http://xclient.info/s/"
    html = getHTMLText(url)
    shuchu = getContent(html)
    for shu in shuchu:
        print("{0:^60}\t{1:^10}".format(shu[0], shu[1], chr(12288)))


main()

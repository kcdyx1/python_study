# coding:utf8
import sys

from jiebafenci import fenci
import jieba
import jieba.analyse

# 建立无意义词列表
stopwords = []
with open("/Users/kangchen/python_study/globaltechmap/spider/extra_dict/stop_words.txt") as file_object:
    while 1:
        word = file_object.readline().replace('\n','').strip()
        stopwords.append(word)
        if not word:
            break

# 输入需要分析的源文件
daifenxi = 'xincailiao_neirong_2017.csv'
fencijieguo = []
stat = {}

with open(daifenxi, 'r') as fr:
    nr = fr.read()
    jieguos = fenci(nr)
    for jieguo in jieguos:
        if jieguo in stopwords:
            continue
        else:
            if jieguo not in fencijieguo:
                fencijieguo.append(jieguo)
            if jieguo not in stat:
                stat[jieguo] = 0
            stat[jieguo] += 1

# 结果排序
stat = sorted(stat.items(), key=lambda d: d[1], reverse=True)

# 结果保存
wenjianjia = "/Users/kangchen/python_study/globaltechmap/spider/Results/" 
fencijieguo_wenjian = wenjianjia + '新材料2017.csv'

with open(fencijieguo_wenjian, 'w') as fw:
    for item in stat:
        fw.write(item[0] + ',' + str(item[1]) + '\n')

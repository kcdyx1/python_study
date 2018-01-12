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

fields ={
        'hy':'haiyang',
        'hk': 'hangkong',
        'ht': 'hangtian',
        'kjzl':'kejizhanlue',
        'ny': 'nengyuan',
        'sw': 'shengwu',
        'xjzz': 'xianjinzhizao',
        'xcl':'xincailiao',
        'xx': 'xinxi'
}

field_alia = input("请输入需要分析的领域首字母：")
field = fields[field_alia]
year = input("请输入需要分析的年份：")

# 输入需要分析的源文件
daifenxi = "/Users/kangchen/python_study/globaltechmap/spider/MySQL_Results/" + field + '_neirong_' + year + '.csv'
fencijieguo = []
stat = {}

with open(daifenxi, 'r') as fr:
    nr = fr.read()
    jieguos = fenci(nr)
    for jieguo in jieguos:
        if jieguo not in stopwords:
            if jieguo not in fencijieguo:
                fencijieguo.append(jieguo)
            if jieguo not in stat:
                stat[jieguo] = 0
            stat[jieguo] += 1

# 结果排序
stat = sorted(stat.items(), key=lambda d: d[1], reverse=True)
print("分析完成，结果正在保存……")
# 结果保存
jieguo_dizhi = "/Users/kangchen/python_study/globaltechmap/spider/Results/" 
fencijieguo_wenjian = jieguo_dizhi + field + year +'.csv'

with open(fencijieguo_wenjian, 'w') as fw:
    for item in stat:
        fw.write(item[0] + ',' + str(item[1]) + '\n')
print("结果保存完毕，请放心食用！")

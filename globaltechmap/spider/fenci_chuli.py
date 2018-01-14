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
fenxideshisha = field + ' ' + str(year)
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

words_list = []
num_list = []
with open(fencijieguo_wenjian, 'w') as fw:
    for item in stat:
        fw.write(item[0] + ',' + str(item[1]) + '\n')
        if item[1] > 25:
            words_list.append(item[0])
            num_list.append(item[1])

panduan = input("是否要保存列表：")
if panduan == 'y':
    liebiaojieguo = jieguo_dizhi + 'liebiao_jieguo.txt'
    with open(liebiaojieguo, 'a') as fw:
        fw.write(fenxideshisha + '\n')
        fw.write('var dataAxis = ' + str(words_list) + ';\n')
        fw.write('var data = ' + str(num_list) + ';\n')
    print("结果保存完毕，请放心食用！")
else:
    print("结果保存完毕，请放心食用！")


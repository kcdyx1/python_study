# coding:utf8

from jiebafenci import fenci
import jieba
import jieba.analyse

jieba.load_userdict("userdict.txt")
jieba.analyse.set_stop_words("stop_words.txt")

with open('xincailiao_neirong_2015.csv', 'r') as fr:
    nr = fr.read()
    # fenci(nr)
    tags = jieba.analyse.extract_tags(nr, topK=100)
    print(",".join(tags))
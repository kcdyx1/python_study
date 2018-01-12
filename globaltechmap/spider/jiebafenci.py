# coding:utf8

import jieba
import jieba.analyse

def fenci(yuanhua):
    jieba.load_userdict("/Users/kangchen/python_study/globaltechmap/spider/extra_dict/userdict.txt")
    jieba.analyse.set_stop_words("/Users/kangchen/python_study/globaltechmap/spider/extra_dict/stop_words.txt")
    content = yuanhua
    clear_content = content.replace('，', '').replace('。', '').replace('“', '').replace('”', '').replace('：', '').replace('《', '').replace('》', '').replace('、', '').replace('（', '').replace('）', '').replace(',', '').replace(' ', '')
    seg_list = jieba.cut(clear_content, cut_all=False, HMM=True)
    return seg_list
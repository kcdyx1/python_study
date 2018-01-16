# coding:utf8

import jieba
import jieba.analyse


def fenci_all(yuanhua):
    # 全模式
    jieba.load_userdict("/Users/kangchen/python_study/globaltechmap/spider/extra_dict/userdict.txt")
    jieba.analyse.set_stop_words("/Users/kangchen/python_study/globaltechmap/spider/extra_dict/stop_words.txt")
    content = yuanhua
    clear_content = content.replace('，', '').replace('。', '').replace('“', '').replace('”', '').replace('：', '').replace('《', '').replace('》', '').replace('、', '').replace('（', '').replace('）', '').replace(',', '').replace(' ', '').replace('；', '')
    seg_list = jieba.cut(clear_content, cut_all=True, HMM=True)
    return seg_list


def fenci(yuanhua):
    # 不同模式分词
    jieba.load_userdict("/Users/kangchen/python_study/globaltechmap/spider/extra_dict/userdict.txt")
    jieba.analyse.set_stop_words("/Users/kangchen/python_study/globaltechmap/spider/extra_dict/stop_words.txt")
    content = yuanhua
    clear_content = content.replace('，', '').replace('。', '').replace('“', '').replace('”', '').replace('：', '').replace('《', '').replace('》', '').replace('、', '').replace('（', '').replace('）', '').replace(',', '').replace(' ', '').replace('；', '')
    seg_list = jieba.cut(clear_content, cut_all=False, HMM=True)
    return seg_list
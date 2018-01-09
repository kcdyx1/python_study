# coding:utf8

import jieba

def fenci(yuanhua):
    content = yuanhua
    clear_content = content.replace('，', '').replace('。', '').replace('“', '').replace('”', '').replace('：', '').replace('《', '').replace('》', '').replace('、', '')
    seg_list = jieba.cut(clear_content, cut_all = False)
    print('\n'.join(seg_list))
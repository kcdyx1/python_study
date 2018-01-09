# coding:utf8

import pymysql

conn = pymysql.connect(host ='localhost', port =8889, user ='root', password ='root', db='globaltechmap', charset='utf8')
cursor = conn.cursor()
# rowNums = cursor.execute('SELECT news_id FROM xincailiao')  
# print('查询的行数为' + str(rowNums)
# conn.close()
sql = "SELECT content FROM xincailiao where date between '2015-01-01' and '2015-12-31'"
words = ()
try:
    cursor.execute(sql)    #执行sql语句 
    results = cursor.fetchall()
    # print(len(results))
    for row in results:
        content = row[0]
        with open('xincailiao_neirong_2015.csv', 'a') as fw:
                 fw.write(content)
        print(content)
except Exception as e:
    raise e
finally:
    conn.close()

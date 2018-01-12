# coding:utf8

import pymysql

conn = pymysql.connect(host ='localhost', port =8889, user ='root', password ='root', db='globaltechmap', charset='utf8')
cursor = conn.cursor()

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

field_alia = input("请输入需要查询的领域首字母：")
field = fields[field_alia]
year_input = input("请输入需要查询的年份：")
year = "'" + year_input

sql = "SELECT content FROM "+ field + " where date between " + year + "-01-01' and " + year + "-12-31'"
words = ()
try:
    cursor.execute(sql)    #执行sql语句 
    results = cursor.fetchall()
    # print(len(results))
    for row in results:
        content = row[0]
        # 保存查询结果

        chaxuejieguo = "/Users/kangchen/python_study/globaltechmap/spider/MySQL_Results/" + field + "_neirong_" + year.replace("'","") + ".csv"
        with open(chaxuejieguo, 'a') as fw:
                 fw.write(content)
    print("中共中央贺电：查询结果已经成功保存！")
except Exception as e:
    raise e
finally:
    conn.close()

#coding:utf-8


filename = 'xyj.txt'

characters = []
stat = {}
with open(filename) as file_object:
    for line in file_object:
        line = line.strip()
        if len(line) == 0:
            continue

        for x in range(0, len(line)):
            if line[x] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……', '[', ']', '/', ':', '-']:
                continue
            if not line[x] in characters:
                characters.append(line[x])
            if not line[x] in stat:
                stat[line[x]] = 0
            stat[line[x]] += 1

stat = sorted(stat.items(), key=lambda d: d[1], reverse=True)

filename1 = 'result.csv'

with open(filename1, 'w') as fw:
    for item in stat:
        fw.write(item[0] + ',' + str(item[1]) + '\n')

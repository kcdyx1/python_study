stopwords = []
with open("/Users/kangchen/python_study/globaltechmap/spider/extra_dict/stop_words.txt") as file_object:
    while 1:
        ci = file_object.readline().replace('\n','').strip()
        if ci not in stopwords:
            stopwords.append(ci)
        else:
            continue
        if not ci:
            break
for s in stopwords:
    print(s)
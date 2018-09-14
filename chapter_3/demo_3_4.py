import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 获取单词的出现情况列表，
            # 如果单词不存在，把单词和一个空列表放进映射，然后返回这个空列表，
            # 这样就能在不进行第二次查找的情况下更新列表了
            # 如果word不在index中，就把word的值设置为[]
            # 如果word在index中，就先返回word对应的value，然后对value追加元素
            index.setdefault(word, []).append(location)

            # 上一行代码的功能与下面三行代码相同
            '''
            if word not in index:
                index[word] = []
            index[word].append(location)
            '''

for word in sorted(index, key=str.upper):
    print(word, index[word])
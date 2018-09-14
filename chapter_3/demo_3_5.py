'''
具体而言，在实例化一个 defaultdict 的时候，需要给构造方法提供一个可调用对象，
这个可调用对象会在 __getitem__ 碰到找不到的键的时候被调用，让 __getitem__ 返回某种默认值。
比如，我们新建了这样一个字典：dd = defaultdict(list)，
如果键 'new-key' 在 dd 中还不存在的话，表达式 dd['new-key'] 会按照以下的步骤来行事。

(1) 调用 list() 来建立一个新列表。
(2) 把这个新列表作为值，'new-key' 作为它的键，放到 dd 中。
(3) 返回这个列表的引用。
而这个用来生成默认值的可调用对象存放在名为 default_factory 的实例属性里。
'''
# 利用 defaultdict 实例而不是 setdefault 方法

import sys
import re
from collections import defaultdict

WORD_RE = re.compile(r'\w+')
# 把 list 构造方法作为 default_factory 来创建一个 defaultdict。
index = defaultdict(list)

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 如果 index 并没有 word 的记录，那么 default_factory 会被调用，为查询不到的键创造一个值。
            # 这个值在这里是一个空的列表，然后这个空列表被赋值给 index[word]，继而被当作返回值返回，
            # 因此 .append(location) 操作总能成功。
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
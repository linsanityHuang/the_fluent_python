import weakref

a_set = {0, 1}

# 创建弱引用对象 wref，下一行审查它
wref = weakref.ref(a_set)

print(wref)

wref()

wref() is None

wref() is None

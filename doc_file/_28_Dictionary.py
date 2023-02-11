#!/usr/bin/python
import random

# mutable sequence(but key is immutable sequence)
# create dic
d = {10: 'dog', 20: 'pet', 10: 'cat', 30: 'zoo'}
print(d)
d = dict(cat=10, dog=20)
print(d)
# tuple could be key,but list can not be key
t = (10, 20)
print({t: 10})
# lst=[10,20]
# print({lst:10})
print(max(d))
del d
# print(d)

# zip func
lst1 = [10, 20, 30, 40]
lst2 = ['cat', 'dog', 'car', 'zoo']
zipobj = zip(lst1, lst2)
print(zipobj)
# print(list(zipobj))
print(dict(zipobj))

# get
d = {'hello': 10, 'world': 20, 'python': 30}
print(d['hello'])
print(d.get('hello'))

# print(d['java']) #error
print(d.get('java'))
print(d.get('java', 'Nope'))

# traversal dict
# 1. for element in d.items(): pass
for e in d.items():
    print(e)
print('>' * 40)
# 2. for k,v in d.items(): pass
for k, v in d.items():
    print(k, v)

# operator
print('-----------------------------------')
d = {1001: 'limei', 1002: 'wanghua', 1003: 'zhangfeng'}
print(d)
# add
d[1004] = 'zhanglili'
print(d)
# keys
keys = d.keys()
print(keys)
print(list(keys))
print(tuple(keys))
items = d.items()
print(items)
print(list(items))
print(tuple(items))
# conversion to dict
lst = list(items)
d = dict(lst)
print(d)
# pop
print(d.pop(1001))
print(d)
print(d.pop(1008, 'None'))
print(d.popitem())
print(d)
d.clear()
print(d)
print(bool(d))

# create dict
print('------------------------------')
d = {item: random.randint(1, 100) for item in range(4)}
print(d)

lst = [1001, 1002, 1003]
lst2 = ['chenmeimei', 'wangyiyi', 'lihaha']
d = {k: v for k, v in zip(lst, lst2)}
print(d)

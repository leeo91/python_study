# -*- coding: utf-8 -*-
# Auther : Zhichao
# Date : 2023/1/13 20:33
# File : string_slice.py
# 0->asc  -10->desc
s = 'HelloWorld'
print(s[0], s[-10])

# slice
print(s[2:7])
print(s[-8:-3])

print(s[:5])
print(s[5:])
print(s[:])

# string operation
x = '2022year'
y = "beijing olympic"

print(x + y)
print(10 * x)
print(x * 10)

print("beijing" in y)
print('shanghai' in y)

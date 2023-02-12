# import my_info
import my_info as a
# from my_info import name, info
from my_info import *
import math, random, os
# 如果导入的模块中有同名的函数等，那么后导入的生效
from introduce import *

print(a.name)
print(a.info())

print('---------------------------------')
print(name)
print(info())

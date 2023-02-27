# os/re/random/json/time
# 1.random
import random
import time

random.seed(10)
print(random.random())
print(random.random())
print('-------------------')
random.seed(10)
print(random.random())
print(random.random())

# [a,b]
print(random.randint(1, 10))
print('-------------------')
for i in range(1, 10):
    print(random.randrange(1, 10, 3), end='\t')

print()
print('--------------------')
# [a,b] 小数
print(random.uniform(1, 100))

print('--------------------')
# 列表随机取数
lst = [i for i in range(1, 11)]
print(random.choice(lst))

random.shuffle(lst)
print(lst)
random.shuffle(lst)
print(lst)
print('+++++++++++++++++++++++++++++++')

# time
now = time.time()
print(now)
obj = time.localtime()
print(obj)
print(type(obj))
print('year:', obj.tm_year)
print(time.ctime())
# time format
print(time.strftime('%Y-%m-%d %H:%M:%S', obj))
print(time.strftime('%B', obj))
print(time.strftime('%A', obj))
print(time.strptime('2008-08-08', '%Y-%m-%d'))
# count time
time.sleep(10)
print('hello world')

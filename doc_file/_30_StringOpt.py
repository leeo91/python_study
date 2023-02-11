s1 = 'HelloWorld'
s2 = s1.lower()
print(s1, s2)

s3 = '中国'
s4 = s3.upper()
print(s3, s4)

s_email = 'zhichao@163.com'
lst = s_email.split('@')
print(s_email, lst)

print(s1.count('o'))
print(s1.count('h'))

print(s1.find('o'))
print(s1.find('p'))

print(s1.index('o'))
# print(s1.index('p')) #ValueError: substring not found

print(s1.startswith('H'))
print(s1.startswith('p'))

print('demo.py'.endswith('.py'))
print('demo.txt'.endswith('.txt'))

s = 'HelloWorld'
new_s = s.replace('o', '*nihao*')
print(s, new_s)

print(s.center(20, '*'))

s = '   dlhello   world   '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = 'dlhelloworld'
print(s.strip('ld'))  # doesn't matter with the order  same with s.strip('dl')
print(s.lstrip('ld'))
print(s.rstrip('ld'))

# format
# %s -> 字符串格式；%d -> 十进制整数格式；%f -> 浮点数
name = 'madongmei'
age = 18
score = 98.5
# 1. %
print('name:%s,age:%d,score:%.1f' % (name, age, score))
# 2. f-string
print(f'name:{name},age:{age},score:{score}')
# 3. template format
print('name:{0},age:{1},score:{2}'.format(name, age, score))  # should care the order

# format func
s = 'helloworld'
print('{0:*<20}'.format(s))
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))
print(s.center(20, '*'))

# thousands separator
print('{0:,}'.format(324233454564456))
print('{0:,}'.format(32423345456.4456))

print('{0:.2f}'.format(3.14159265))
print('{0:.6}'.format(3.14159265))

a = 425
# c-> unicode
print('{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}'.format(a))
b = 3.1415926
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))

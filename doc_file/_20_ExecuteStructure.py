# 1.Sequential Structure
"""元组分解赋值： name,age='zhangsan',20
列表分解赋值：[name,age]=['zhangsan',20]
字符串分解赋值：a,b,c,d='room'
序列解包赋值：a,*b='room'
"""
name = 'zhangsan'
age = 20
a = b = c = d = 100
name1, age1 = 'lisi', 22  # 元组分解赋值
[name2, age2] = ['lisi', 22]
a, b, c, d = 'room'
a, *b = 'room'
name = input('pls input:')
print(name)

# 2.Select Structure
''' 
if 表达式：
  执行语句
'''
number = eval(input('pls input the six lucky number:'))
if number == 123456:
    print('Congratulations')
if number != 123456:
    print('Doesn\'t win the lottery')

if a > b:
    print('a>b')
else:
    print('a<b')

result = 'success' if number == 22 else 'failed'
print(result)

if number > 100 or number < 0:
    print('error')
elif 90 < number <= 100:
    print('A')
elif 80 < number <= 90:
    print('B')
elif 70 < number <= 80:
    print('C')
elif 60 < number <= 70:
    print('D')
else:
    print('E')

# 3.Cyclic Structure
'''
for v in list:
  expression
遍历对象：字符串、文件、组合数据类型、range()函数

range(),产生一个[n,m)的整数序列，包含n，不包含m
for i in range(1,11):
  print(i)
  
while a>b:
  expression
'''
for i in range(1, 10):
    j = i
    while (j <= 9):
        print(str(i) + ' * ' + str(j) + ' = ', i * j, end=' ')
        j += 1
    print('\n')

# for和while循环的扩展模式,通常与break和continue语句一起使用
for v in list:
    expression1
else:
    expression2

while a > b:
    expression1
else:
    expression2

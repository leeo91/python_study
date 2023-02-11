# immutable sequence
t1 = ('hello', [10, 20, 30], 'python', 12)
print(t1)
t = tuple('hello')
print(t)
t = tuple([1, 2, 3, 4, 5])
print(t)
t = tuple(range(1, 10))
print(t)

print(10 in t)
print(10 not in t)
print(max(t))
print(min(t))
print(len(t))
print(t.index(1))
print(t.count(3))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# should keep ","
x = (10)
print(x, type(x))
y = (10,)
print(y, type(y))

del t
# print(t)


# add/update/del/get tuple
t = ('python', 'hello', 'world')
print(t[0])
t2 = t[0:3:2]
print(t2)

# traversal tuple
for item in t:
    print(item)

for i in range(len(t)):
    print(i, t[i])

for k, v in enumerate(t, 1):
    print(k, '---->', v)

# create tuple
print('-' * 40)
t = (i for i in range(1, 11))
print(t)
# t1=tuple(t)
# print(t1)
# for item in t:
#     print(item)
print('>' * 40)

print(t.__next__())
print(t.__next__())
print(t.__next__())

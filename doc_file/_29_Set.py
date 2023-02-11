# 1.assignment first
s = {1, 2, 3, 4}
print(s)

# s = {[1, 2], [3, 4]}
# s = {([1, 2]), ([3, 4])}
s = {(1, 2), (3, 4)}
print(s)

s = {}
print(type(s))

# 2.assignment second
s = set()
print(type(s), bool(s))

# create func
# duplicate removal
s = set('helloworld')
s2 = set([10, 20, 30])
s3 = set(range(1, 10))
print(s)
print(s2)
print(s3)

# belongs to sequence
print(max(s3))
print(len(s3))
print(9 in s3)
print(9 not in s3)

# del collection
del s3
# print(s3)


# set operation
A = {10, 20, 30, 40, 50}
B = {30, 50, 88, 76, 20}
print(A & B)
print(A | B)
print(A - B)
print(A ^ B)

s = {10, 20, 30}
s.add(100)
print(s)
s.remove(20)
print(s)
s.clear()
print(s, bool(s))

# traversal set
s = {10, 20, 30}
for item in s:
    print(item)

for k, v in enumerate(s, 10):
    print(k, '-->', v)

# create set
s = {i for i in range(10)}
print(s)
s = {i for i in range(10) if i % 2}
print(s)

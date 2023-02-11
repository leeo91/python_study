x = 20
y = 10
x += y
print(1, x, y)
x -= y
print(2, x, y)
x *= y
print(3, x, y)
x /= y
print(4, x, y)
x %= y
print(5, x, y)
z = 3
y //= z
print(6, y)
y **= 2
print(7, y)

# chain assignment
a = b = c = 100
print(a, b, c)
# unpackage assignment
a, b = 10, 20
print(a, b)
# variable exchange
a, b = b, a
print(a, b)

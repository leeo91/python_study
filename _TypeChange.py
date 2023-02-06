# -*- coding: utf-8 -*-
# Auther : Zhichao
# Date : 2023/1/13 20:48
# File : type_exchange.py
# implicit type conversion
x = 10
y = 3
z = x / y
print(z)

# display type conversion
character = chr(38)
print(character)
# float -> int, just keep the integer part
print('float -> int:', int(3.14))
print('float -> int:', int(3.9))
print('float -> int:', int(-3.14))
print('float -> int:', int(-3.9))
# int -> float
print('int -> float:', float(10))
# str -> int
print(int('100') + int('200'))
# str -> float
print('str -> float:', float('3.14'))
# str -> int/float (with errors)
# print(int('18a'))
# print(int('3.14'))


# chr and ord(the conversion of character and integer)
print(ord('h'))
print(chr(104))

# int/float/str/chr/ord/hex/oct/bin
print('int -> hex:', hex(104))
print('int -> octal:', oct(104))
print('int -> binary:', bin(104))

a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c)

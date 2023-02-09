# and/or/not
print(True and True)
print(True and False)
print(False and False)
print('---------------')
print(8>7 or 6>5)
print(8>7 or 6<5)
print(8<7 or 6<5)
print('---------------')
print(not 6>5)
print(not 6<5)
print('---------------')
print(8>7 or 10/0)  # the second expression doesn't execute
print(8<7 and 10/0)

import random

count = 0
num = -1
ran = random.randint(1, 100)
while num != ran:
    if 0 < num < ran:
        print('less')
    if num > 0 and num > ran:
        print('more')
    num = eval(input('pls input number:'))
    count += 1
print('guess count:', count)

lenthth = eval(input('pls input:'))
while lenth % 2 == 0:
    print('The input number is error, pls input again')
    lenth = eval(input('input again:'))
top = (lenth + 1) // 2
for i in range(1, top + 1):
    for j in range(1, top + 1 - i):
        print(' ', end='')
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

bottom = lenth // 2
for i in range(1, bottom + 1):
    for j in range(1, i + 1):
        print(' ', end='')
    for k in range(1, lenth - 2 * i + 1):
        if k == 1 or k == lenth - 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

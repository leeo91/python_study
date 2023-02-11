inputStr = input('pls input the string:')
designatedStr = input('pls input designated string:')
count = 0
len1 = len(designatedStr)

for i in range(len(inputStr)):
    str1 = inputStr[i:(i + len1)]
    if str1 == designatedStr:
        count += 1

print('The total count is:', count)


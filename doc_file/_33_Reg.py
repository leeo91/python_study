import re

# match->true   not match->None
pattern = r'\d\.\d+'
s = 'I study python3.10'
match = re.match(pattern, s, re.I)
print(match)

s2 = '3.10python I study'
match2 = re.match(pattern, s2, re.I)
print(match2)
print(match2.start())
print(match2.end())
print(match2.span())
print(match2.string)
print(match2.group())

# search
s = 'study python3.10 everyday python 2.10'
s2 = '4.10 study every day'
s3 = 'study python'
match = re.search(pattern, s)
match2 = re.search(pattern, s2)
match3 = re.search(pattern, s3)

print(match)
print(match2)
print(match3)

# findAll
s = 'study python3.10 everyday python 2.10'
s2 = '4.10 study every day'
s3 = 'study python'
lst = re.findall(pattern, s)
lst2 = re.findall(pattern, s2)
lst3 = re.findall(pattern, s3)

print(lst)
print(lst2)
print(lst3)

# sub
pattern = 'hack|crack|python'
s = 'I want study python, could I be a hacker'
new_s = re.sub(pattern, 'XXX', s)
print(new_s)

# split
s2 = 'https://www.baidu.com/s?wd=ysj&ie=utf-8&tn=baidu'
pattern2 = '[?|&]'
lst = re.split(pattern2, s2)
print(lst)

pattern3 = r'13[4-9]\d{8}'
lst = ['13809876543', '15109876543']
for item in lst:
    match = re.match(pattern3, item)
    if match is not None:
        print(match.group())

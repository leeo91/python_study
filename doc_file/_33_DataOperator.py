# str concat
s1 = 'hello'
s2 = 'world'
# 1. +
print(s1 + s2)
# 2.join
print(''.join([s1, s2]))
print('*'.join([s1, s2, 'python']))
# 3.concat directly
print('hello''world')
# 4.format str
print('%s%s' % (s1, s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1, s2))

# str duplicate removal
s = 'fsdfwer21rdsfasdwrqwetrf'
new_s = ''
for item in s:
    if item not in new_s:
        new_s += item
print(new_s)

new_s2 = ''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2 += s[i]
print(new_s2)

new_s3 = set(s)
lst = list(new_s3)
lst.sort(key=s.index)
print(''.join(lst))

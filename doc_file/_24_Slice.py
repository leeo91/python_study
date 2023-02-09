s='HelloWorld'
s1=s[0:5:1]  #start 0,end 5, step 1
print(s1)
#ellipsis start number
print('1',s[:5:1])
print('2',s[:5])
print('3',s[0::1])
print('4',s[5:])
print('5',s[:5:2])
print('6',s[::2])

#the step can be negtive
print(s[::-1])

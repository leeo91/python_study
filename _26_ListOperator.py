#list -> variable sequence
lst=['hello','world',99.8,100]
lst1=list('helloworld')
lst2=list(range(1,10,2))

print(lst1)
print(lst2)

print('-'*40)
print(lst1+lst2)
print(lst2*3)
print(lst2.index(3))

print('-'*40)
lst3=[10,23,55]
print(lst3)
lst3.append('Runoob')
print(lst3)
del lst3[2]
print(lst3)
del lst3
#print(lst3)

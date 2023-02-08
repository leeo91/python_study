import random

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
#add/del/update/get list
lst3=[10,23,55]
print(lst3)
lst3.append('Runoob')
print(lst3)
lst3.insert(3,'xxx')
print(lst3)
lst3.insert(3,'xxx')
print(lst3)
lst3.remove('xxx')
print(lst3)
lst3.pop(1)
print(lst3)
lst3.reverse()
print(lst3)
del lst3[2]
print(lst3,id(lst3))
newList = lst3.copy()
print(newList,id(newList))
lst3.clear()
print(lst3)
del lst3
#print(lst3)

print('-'*40)
#sort list
# 1.sort
lst=['banana','apple','Cat','orange']
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
lst.sort(key=str.lower)
print(lst)
# 2.sorted
print('>'*40)
lst=['banana','apple','Cat','orange']
print(lst)
asc_lst=sorted(lst)
print(asc_lst)
desc_lst=sorted(lst,reverse=True)
print(desc_lst)
new_lst=sorted(lst,key=str.lower)
print(new_lst)


print('-'*40)
#create list
lst6=[item for item in range(1,11)]
print(lst6)
lst6=[item*item for item in range(1,11)]
print(lst6)
#item could be empty
lst6=[random.randint(1,10) for _ in range(10)]
print(lst6)
#if condition
lst=[item for item in range(10) if item%2==0]
print(lst)


# traversal list
# 1. for... in...
print('-'*40)
lst=['hello','world',99.8,100]
for item in lst:
    print(item)
# 2. for and range(),len(), cycle by index
print('-'*40)
for i in range(len(lst)):
    print(i,'-->',lst[i])
# 3.enumerate
print('-'*40)
for index,item in enumerate(lst,10):
    print(index,'-->',item)


#two-dimensional list
lst=[['city','x','y'],['beijing',101,106]]
print(lst)
lst=[[j for j in range(5)] for i in range(4)]
print(lst)
for i in lst:
    for j in i:
        print(j,end=' ')
    print()

file = input('pls input: ')
print('the input value is: ', file)

file = open('note.txt', 'w')
print('beijing, welcome', "hello", sep='\t xxx', end='\r --->', file=file)
file.close

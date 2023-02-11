print('123'.isdigit())  # arabic numbers  True
print('一二三'.isdigit())
print('0b1001'.isdigit())
print('ⅠⅠⅠⅠⅠ'.isdigit())
print('-----------------------------------')
print('123'.isnumeric())  # True
print('一二三'.isnumeric())  # True
print('0b1001'.isnumeric())
print('ⅠⅠⅠⅠⅠ'.isnumeric())  # True
print('壹贰叁肆'.isnumeric())  # True
print('----------------------------------')
print('helloi你好'.isalpha())  # True
print('helloi你好123'.isalpha())
print('helloi你好一二三'.isalpha())  # True
print('helloi你好ⅠⅠⅠ'.isalpha())
print('---------------------------------------')
print('hello123'.isalnum())  # True
print('hello123...'.isalnum())
print('hello一二三'.isalnum())  # True
print('hello壹贰叁'.isalnum())  # True
print('helloⅠⅠⅠ'.isalnum())  # True
print('---------------------------------------')
print('Hello123'.islower())
print('hello123...'.islower())  # True
print('hello一二三'.islower())  # True
print('HEELO一二三'.islower())  # True
print('---------------------------------------')
print('HelloWorld'.istitle())
print('Hello World'.istitle())  # True
print('Hello world'.istitle())
print('Helloworld'.istitle())  # True
print('---------------------------------------')
print('\t'.isspace())  # True
print('   '.isspace())  # True
print('\n'.isspace())  # True

import json


# One/Two dimensional data
def my_write():
    lst = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
    with open('stu.csv', 'w') as file:
        file.write(','.join(lst))


def my_read():
    with open('stu.csv', 'r') as file:
        s = file.read()
        lst = s.split(',')
        print(lst)


my_write()
my_read()


def my_write_table():
    lst = [
        ['product', 'unitPrice', 'count'],
        ['cup', '8', '20'],
        ['mouse', '77', '29']
    ]
    with open('table.csv', 'w') as file:
        for item in lst:
            line = ','.join(item)
            file.write(line)
            file.write('\n')


def my_read_table():
    data = []
    with open('table.csv', 'r') as file:
        lst = file.readlines()
        for item in lst:
            new_lst = item[:len(item) - 1].split(',')
            data.append(new_lst)
    print(data)


my_write_table()
my_read_table()

# json format
lst = [
    {'name': 'ysj', 'age': 18, 'score': 90},
    {'name': 'cmm', 'age': 12, 'score': 95},
    {'name': 'lyy', 'age': 20, 'score': 20}
]
# ensure_ascii=False 中文展示
# indent=4 缩进美观
s = json.dumps(lst, ensure_ascii=False, indent=4)
print(type(s))
print(s)

lst2 = json.loads(s)
print(type(lst2))
print(lst2)

with open('stu.txt', 'w') as file:
    json.dump(lst, file, indent=4, ensure_ascii=False)

with open('stu.txt', 'r') as file:
    print(json.load(file))

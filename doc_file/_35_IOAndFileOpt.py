# text file(x.txt)/binary file(word,pdf,mp3...)
# 1.operate file
def my_write():
    file = open('x.txt', 'w', encoding='utf-8')
    file.write('The great China dream!')
    print('\rthanks', file=file)
    file.close()


def my_read():
    file = open('x.txt', 'r', encoding='gbk')
    # s = file.read()
    # print(s)
    print('--------------------')
    lst = file.readlines()
    for item in lst:
        print(item)
    file.close()


my_write()
my_read()

# the file open mode
"""
1.r -> 以只读模式打开，文件指针在文件的开头，如果文件不存在，程序抛出异常
2.rb -> 以只读模式打开二进制文件，如图片文件
3.w -> 覆盖写模式，文件不存在创建，文件存在则内容覆盖
4.wb -> 覆盖写模式写入二进制数据，文件不存在则创建，文件存在则覆盖
5.a -> 追加写模式，文件不存在就创建，文件存在则在文件最后追加内容
6.+ -> 与w/r/a等一同使用，在原功能的基础上增加同时读写功能
"""
# the method of read/write file
"""
1.file.read(size) -> 从文件中读取size个字节或字符，如果没给参数则读取全部内容
2.file.readline(size) -> 读取文件中一行数据，如果给定参数则读取一行中的size个字符或字节
3.file.readlines() -> 从文件中读取所有内容，结果为列表类型
4.file.write(s) -> 将字符串s写入文件
5.file.writelines(lst) -> 将内容全部为字符串列表lst写入到文件
6.file.seek(offset) -> 改变当前文件操作指针的位置，英文占一个字节，中文gbk编码占两个字节，utf-8编码占三个字节
"""


def write_list(name, lsts):
    file = open(name, 'w', encoding='utf-8')
    file.writelines(lsts)
    file.close()


lst = ['name\t', 'age\t', 'score\r', 'zhangsan\t', '20\t', '99']
write_list('y.txt', lst)


# copy file
def copy(src, new_path):
    file1 = open(src, 'rb')
    s = file1.read()
    file2 = open(new_path, 'wb')
    file2.write(s)
    file2.close()
    file1.close()

copy('../images/data_type.PNG','copy.png')


# with -> will always close the file
"""
with open(...) as file:
    pass
"""
def copy_file(src,target):
    with open(src,'r') as file1:
        with open(target,'w') as file2:
            file2.write(file1.read())

copy('x.txt','u.txt')

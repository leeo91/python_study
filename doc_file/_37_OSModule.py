import os
import time

# os
"""
getcwd()/listdir(path)/mkdir(path)/makedirs(path)
rmdir(path)/removedirs(path)/chdir(path)/walk(path)
"""
print('work dir:', os.getcwd())
print('directory and file:', os.listdir())

# os.mkdir('./test/hello')
# os.makedirs('./test/hello/ti/t2')

# os.rmdir('./test')
# os.removedirs('./test/hello/ti/t2')

os.chdir('D:/')
print(os.getcwd())

for dirs, dirlst, filelst in os.walk('D:\exeInstall\python\python_learning\learning_doc\python_study\doc_file'):
    print(dirs)
    print(dirlst)
    print(filelst)
    print('------------------------------')


# file operation
os.chdir('D:\exeInstall\python\python_learning\learning_doc\python_study\doc_file')
# remove
# os.remove('a.txt')
# rename
# os.rename('y.txt', 'yy.txt')
# get file info
info = os.stat('./yy.txt')
print(type(info))
print(info)
print('the latest query time is:', info.st_atime)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info.st_atime)))


# start the app
os.startfile('calc.exe')


# os.path module
"""
abspath(path)/exists(path)/join(path,name)/splitext()
basename(path)/dirname(path)/isdir(path)/isfile(file)
"""
print('+++++++++++++++++++++++++++++++++++++++++++')
print('get the absolute file path:', os.path.abspath('x.txt'))
print('is exists:', os.path.exists('stu.txt'))
print('is exists:', os.path.exists('test'))
print('suffix:', os.path.splitext('x.txt'))
print('file name:', os.path.basename(r'D:\exeInstall\python\python_learning\learning_doc\python_study\doc_file\x.txt'))
print('file name:', os.path.dirname(r'D:\exeInstall\python\python_learning\learning_doc\python_study\doc_file\x.txt'))


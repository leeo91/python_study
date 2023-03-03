# 1.单下划线：表示protected受保护成员，只允许类本身和子类进行访问，可以通过对象名去访问
# 2.双下划线：表示private私有成员，只允许定义该方法的类本身访问，不能通过类的对象访问，但可以通过“对象名._类名__XXX"方式访问
# 3.首尾双下划线：表示特殊的方法，一般是系统定义的名字
class Student():
    # 首尾双下划线
    def __init__(self, name, age, gender):
        self._name = name  # protected
        self.__age = age  # private
        self.gender = gender

    def _fun1(self):  # protected
        print('self and children access')

    def __fun2(self):  # private
        print('self access')

    def show(self):
        self._fun1()
        self.__fun2()
        print(self._name)
        print(self.__age)


if __name__ == '__main__':
    stu = Student('hmm', 20, 'female')
    print(stu._name)
    # print(stu.__age)

    stu._fun1()
    # stu.__fun2()
    print(stu._Student__age)  # 不建议

    stu._Student__fun2()  #不建议

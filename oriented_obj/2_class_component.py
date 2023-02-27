class Student:
    # 类属性：类中，方法外
    school = 'dzu'

    # 实例属性
    def __init__(self, xm, age):
        self.name = xm  # 将局部变量赋值给实例变量
        self.age = age

    # 实例方法
    def show(self):
        print(f'my name is:{self.name}, age is: {self.age}')
        return 0

    # 类方法
    @classmethod
    def clm(cls):
        print('this is a class method, can not invoke instance\'s attribute and method')
        # print(self.name)

    # 静态方法
    @staticmethod
    def sm():
        print('this is a static method, can not invoke instance\'s attribute and method')
        # print(self.name)


# 类的组成部分的使用
# 创建对象
st = Student('zhangsan', 15)
print(st.name, st.age)
print(Student.school)
print(st.show())
print(Student.clm())
print(Student.sm())

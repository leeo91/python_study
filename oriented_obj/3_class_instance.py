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


# 创建多个对象
st1 = Student('zs', 18)
st2 = Student('ls', 28)
st3 = Student('ww', 20)
st4 = Student('zl', 19)
print(type(st1))
print(type(st2))
print(type(st3))
print(type(st4))

Student.school = 'haward'
print(st1.name, st1.age, st1.school)

# 将对象放到组合数据类型中存储，存储到列表中
lst = [st1, st2, st3, st4]
for item in lst:
    item.show()

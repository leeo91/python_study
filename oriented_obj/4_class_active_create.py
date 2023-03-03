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


stu1 = Student('zs', 18)
stu2 = Student('hmm', 20)
print(stu1.name, stu1.age)
print(stu2.name, stu2.age)

stu2.gender = 'male'
print(stu2.name, stu2.age, stu2.gender)


def introduce():
    print('this is a active method')
    return 1


stu2.fun = introduce

stu2.fun()

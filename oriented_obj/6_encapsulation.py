class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show(self):
        print(f'my name is:{self.__name}, my age is:{self.__age}')


if __name__ == '__main__':
    stu = Student('cmm', -23)
    stu.show()



class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 130:
            print('age not in the right range.')
            self.__age = 18
        else:
            self.__age = value

    def show(self):
        print(f'my name is:{self.__name}, my age is:{self.__age}')


if __name__ == '__main__':
    stu1 = Student('hmm')
    stu1.age = 23
    print(stu1.age)

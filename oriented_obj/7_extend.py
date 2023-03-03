class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"hello, my name is {self.name}, my age is {self.age}")


class Student(Person):
    def __init__(self, name, age, stuno):
        super().__init__(name, age)
        self.stuno = stuno


class Doctor(Person):
    def __init__(self, name, age, department):
        Person.__init__(self, name, age)
        self.department = department


if __name__ == '__main__':
    stu = Student('cmm', 20, '001')
    stu.show()
    doc = Doctor('zs', 23, 'wk')
    doc.show()

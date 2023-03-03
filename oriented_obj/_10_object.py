print(dir(object))


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'my name is {self.name}, my age is {self.age}')

    def __str__(self):
        return 'this is override str method'


if __name__ == '__main__':
    person = Person('hmm', 20)
    print(person.__hash__())
    print(dir(person))
    print('======================')
    print(person)  # call the __str__ method
    print(person.__str__())
    print('=======================')
    print(person.__dir__())  # the same with dir()
    print(dir(person))

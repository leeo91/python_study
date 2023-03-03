class Person:
    def __init__(self, name):
        self.name = name


class A:
    pass


class B(Person, A):
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p = Person('zs')
    a = A()
    b = B('hmm', 18)
    print(a.__dict__)
    print(b.__dict__)
    print(a.__class__)
    print(b.__class__)
    print(p.__class__)
    print(Person.__bases__)
    print(A.__bases__)
    print(B.__bases__)
    print(Person.__base__)
    print(A.__base__)
    print(B.__base__)
    print('------------------------')
    print(A.__mro__)
    print(B.__mro__)
    print(Person.__mro__)

    print('------------------------')
    print(Person.__subclasses__())
    print(B.__subclasses__())
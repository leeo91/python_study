class Animal:
    def eat(self):
        pass


class Person(Animal):
    def eat(self):
        print('eat rice')


class Cat(Animal):
    def eat(self):
        print('cat, like fish')


class Dog(Animal):
    def eat(self):
        print('dog, like bones')


# def fun(obj):
#     obj.eat()


if __name__ == '__main__':
    per = Person()
    cat = Cat()
    dog = Dog()

    per.eat()

    # fun(per)
    # fun(cat)
    # fun(dog)

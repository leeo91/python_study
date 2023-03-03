class FatherA():
    def __init__(self, name):
        self.name = name

    def showA(self):
        print('this is A method')

class FatherB():
    def __init__(self, age):
        self.age = age

    def showB(self):
        print('this is B method')


class Son(FatherA, FatherB):
    def __init__(self, name, age, gender):
        FatherA.__init__(self, name)
        FatherB.__init__(self, age)
        self.gender = gender


if __name__ == '__main__':
    son = Son('hmm', 23, 'female')
    son.showA()
    son.showB()
    
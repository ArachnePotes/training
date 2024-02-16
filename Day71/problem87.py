'''
Question:

Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.
'''

class Person:
    def __init__(self,gender):
        self.gender = gender
    def getGender(self):
        print(f' {self.gender} ')
class Male(Person):
    def __init__(self,name):
        super().__init__('Male')
        self.name = name
    def getGender(self):
        print(f' {self.name} is {self.gender}')

class Female(Person):
    def __init__(self,name):
        super().__init__('Female')
        self.name = name
    def getGender(self):
        print(f' {self.name} is {self.gender}')
print(' socrates is a Person of gender ')
socrates = Person('Null').getGender()
socrates = Male('socrates').getGender()
socrates = Female('socrates').getGender()

'''

Question:
Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.

'''

class American():
    def __init__(self,Nationality):
        self.Nationality = Nationality
        self.age = 21
        self.gender = "Male"
        

    def printNationality(self):
        return print(f"\ni'm a {self.age} {self.Nationality} {self.gender}.\n")
 

class NewYorker(American):
    def __init__(self,name):
        self.name = name
        self.age = 21
        self.gender = "Male"
        super().__init__('American')
    def PrintName(self):
        return print(f"Hello there , i'm {self.name}")

siendfield = NewYorker('jerry')
siendfield.PrintName()
siendfield.printNationality()

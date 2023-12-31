"""
7.2

Question:
Define a class named American which has a static method called printNationality.
Hints:
Use @staticmethod decorator to define class static method.
"""
class American():
    def __init__(self,Nationality):
        self.Nationality = Nationality
        self.age = 21
        self.gender = "Male"
        

    def printNationality(self):
        return print(f"\ni'm a {self.age} {self.Nationality} {self.gender}.\n")
    
a = American("Colombian")
a.printNationality()
'''Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''
class myclass():
    def __init__(self):
        self.string = " "
    
    def getString(self):
        self.string = input("enter string: ")

    def printString(self):
        print(f"""{self.string.upper()}""")

test = myclass() 
test.string = "test1"
print(f""" test string: test1  {test.printString()} """)


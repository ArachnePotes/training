'''

Question:
Define a class named Circle which can be constructed by a radius.
 The Circle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

Solution:

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print aCircle.area()

'''
import numpy as np



class Circle():
    
    def __init__(self,radius) -> None:
        self.radius = radius

    def area(self):
        return print(f"Area: {np.pi*pow(self.radius,2)} \nSimple area : {self.radius**2*3.14}") 


aCircle = Circle(2)
aCircle.area()

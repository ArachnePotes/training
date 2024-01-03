'''

Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area. 

Hints:

'''

class Rectangle():
    def __init__(self,length,width ) -> None:
        self.length = length 
        self.width = width
    def area(self):
        return print(f"Area : {self.length*self.width} ")
    
s = Rectangle(2,3)
s.area()

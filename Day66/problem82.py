'''
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

Hints:
Use list comprehension to make an array.

Solution:

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print array
'''
import numpy as np 
# inhomogeneous  array to be done with numpy
x = [[ 0 for i in range(3)], [ 0 for i in range (5)] , [0 for i in range(8)] ] 
print(type(x), x)

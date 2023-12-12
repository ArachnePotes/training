'''
Question 21
Level 3

Question£º
A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute
the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

import numpy as np
from  numpy.matlib import sqrt

vert,horz = [0] ,[0]

while True:
    pos = input("UP, DOWN, LEFT and RIGHT with a given steps. \n-->")
    if pos:
        p = pos.split(' ')
        facing,steps = p[0],int(p[1])
        if (facing == 'DOWN') or (facing == 'LEFT'):
            steps *= -1
        if facing in [ 'UP', 'DOWN']:
            vert.append(steps)
        if facing in [ 'LEFT', 'RIGHT']:
            horz.append(steps)
    else:
        break

x = np.array(horz)
y = np.array(vert)
d = np.sqrt( pow(x.sum(),2) + pow(y.sum(),2) )
print( int(d))

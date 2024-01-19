'''
Question:

Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.

'''

def function(n):
    if n<= 0:
        return 1
    else:
        return function(n-1) + 100

print(f"{function(int(input('enter a number -->')) )-1}")
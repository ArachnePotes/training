'''
Question:

Please write a program to print the running time of execution of "1+1" for 100 times.



Hints:
Use timeit() function to measure the running time.

'''

def f(x):
     return 1+1 
     
import timeit
print(timeit.repeat("for x in range(100): f(x)", "from __main__ import f",number=100000))


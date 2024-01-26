'''
Question:

Please write a program to output a random even number between 0 and 10 inclusive
using random module and list comprehension.
Hints:
Use random.choice() to a random element from a list.
'''
import random as rd
e = [i for i in range(11) if i%2 == 0 ]
val = (rd.choice(e))
print(f'Elements {e}\nChoice : {val}')

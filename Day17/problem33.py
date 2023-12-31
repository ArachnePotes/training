'''
Question33:
Define a function which can print a dictionary where the keys 
are numbers between 1 and 20 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
'''

def myfunction():
    d = { i:pow(i,2) for i in range(1,21) }
    for i in d:
        print(f'{i} : { d[i]}')

myfunction()


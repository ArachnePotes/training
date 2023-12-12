'''
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
'''
def numbers(n):
    for i in range(0,n+1):
        if (i % 7) == 0:
            print(i)
        else:
            continue
    
numbers(100)

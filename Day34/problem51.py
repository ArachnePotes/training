'''
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions
'''

def throw():
    return (5/0)

try:
    throw()
except ZeroDivisionError:
    print("division by zero!")
except Exception and MemoryError:
    print("caught an exeption!")
finally:
    print( "Ln finally block for cleanup !")

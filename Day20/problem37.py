'''

Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 
(both included). Then the function needs to print all values except the first 5 elements in the list.

'''

def function():
    l = [pow(i,2)for i in range(1,21)]
    return print(l[5::])

function()

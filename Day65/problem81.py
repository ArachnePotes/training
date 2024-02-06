'''
Question:

By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

Solution:
'''

l = [12,24,35,70,88,120,155]
li = [ val for i,val in enumerate(l) if ( (i%2!=0) and (i != 0))]
print(f" Default {l} \n Parsed {li} ")


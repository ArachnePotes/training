'''
Define a function that can accept two strings as input 
and print the string with maximum length in console.
If two strings have the same length, 
then the function should print all strings line by line.

Hints:

Use len() function to get the length of a string
'''
def liner(s1):
    for line in s1:
        print(line)

def problem(s1,s2):
    l1,l2 = len(s1),len(s2)
    if l1>l2:
        return print(s1)
    elif l2>l1:
        return print(s2)
    else:
        return liner(s1+s2)
    

s1 =input("enter string 1-->" )
s2 =input("enter string 2-->" )

problem(s1,s2)

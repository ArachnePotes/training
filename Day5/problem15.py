'''
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

def calculate(a):
    n=a
    d=a*10+a
    c=a*100+a*10+a
    m=a*1000+a*100+a*10+a
    return n+d+c+m

print(calculate(int(input(f"Enter the value of 'a' for a+aa+aaa+aaaa. \n-->"))))


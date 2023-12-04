'''
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def fact(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n*fact(n-1)
    
print(f"""
        test1: {fact(8)} == 40320   (8!)
        test2: {fact(5)} == 120     (5!)
        test3: {fact(10)} == 3628800    (10!)
        test4: {fact(70)} == 1.1978571669¹⁰⁰    (70!)
        test5:  {fact(int(input("manual input: Positive number lessthan and morethan it's not on my  keyborad at the moment :( ")))}
      """)


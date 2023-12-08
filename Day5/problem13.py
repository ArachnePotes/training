'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''


import re 
  
string = input("enter a sentence -->").lower()
pattern1 = "[a-z]"
pattern2 = "[0-9]"
LETTERS = len(re.findall(pattern1, string) )
DIGITS = len(re.findall(pattern2, string) )
print(f'''
        LETTERS {LETTERS}
        DIGITS {DIGITS}
      ''')
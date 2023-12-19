'''Question:
Define a function that can receive two integral numbers in string 
form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.
'''

line = input(' two integral numbers to sum , like "5,6,...n" \n-->').split(',')

sol = [ int(i) for i in line ]

print(sum(sol))

'''
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
'''

heads,legs = int(input("enter the number of heads: ")),int(input("enter the number of legs: "))
if (legs % 2!=0) or (heads == 0) or (legs == 0) or (legs < heads):
    print("Invalid, theres no solution")
else:
    r = ( legs - 2*heads)/2
    c = heads - r
print(f'chikens {c}, rabits {r}')
    


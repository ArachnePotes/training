'''

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
'''

numbers = [ i for i in range(2000,3201)]
#print(numbers[0],numbers[-1])
# find all  --: another list
# such numbers which are divisible by 7 but are not a multiple of 5

l = []
for n in numbers:
    if (n % 7) == 0:
        if (n % 5) != 0:
            l.append(n)
        else:
             continue
print(l)
test1 = [ i/5 for i in l]
print(test1)


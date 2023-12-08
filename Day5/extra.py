'''
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

l = input("comma-separated numbers -->").split(',')
li = [int(i) for i in l]
odd_num = list(filter(lambda x: (x%2==1),li))
pr = [ i*i for i in odd_num]
print(pr)
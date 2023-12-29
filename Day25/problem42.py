'''
Question:
Write a program which can filter even numbers in a list 
by using filter function. 
list is: [1,2,3,4,5,6,7,8,9,10].
'''

li = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x: (x%2==0),li))

print(even)

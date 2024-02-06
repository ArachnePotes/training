'''
Question:

Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.

Solution:
'''

subject = [ 'I' , 'You']
verb = ['Play','Love']
obj  = [ 'Hockey','Football']

sentence = ' '
for count,value in enumerate(subject,start=0):
    sentence = value + verb[count] + obj[count] +  "."
    print(f"{ ' '.join(sentence)}")


'''

Question:

Please write a program which prints all permutations of [1,2,3]


Hints:
Use itertools.permutations() to get permutations of list.

'''

from itertools import permutations as P

l = [1,2,3]
perm = P(l)
print(list(perm))

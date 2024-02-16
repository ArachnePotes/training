'''
Question:

By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

Hints:
Use list's remove method to delete a value.
o el que no es ;)
'''

l =  [12,24,35,24,88,120,155]
l = [ i for i in l if i!=24]
print(f'''
     - Hey Mark can you :
    * By using list comprehension, 
    "please write a program to print the list after removing the value 24"
    in [12,24,35,24,88,120,155].
    - Here is your precious list. 
    \n\t{l}
    significa : me importa un culo lo que tenga. 
    no tiene 24, no tiene cara. ''')

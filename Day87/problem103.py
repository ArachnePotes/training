'''
 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
'''


VOCALS = ['a','e','i','o','u']

def isVocal(c):
    if c in VOCALS:
        return True
    else:
        return False
    
def isVocalList(s):
    l = [ isVocal(i) for i in s]
    return l

s = input(' entra un carácter yo te digo si es una vocal,\n si pones mas que sea separados por "," --> ').split(',')

print(isVocalList(s))
for i in s:
    print(isVocal(i))

'''
Definir una función que calcule la longitud de una lista o una cadena dada.
'''

def longitud_str(s):
    counter = 0
    for i in s:
        counter += 1
    return counter

s = list(input("entra una cadena , yo te  digo cuantos caracteres tiene -> "))
print(longitud_str(s))
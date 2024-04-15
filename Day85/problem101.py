'''
1 - Definir una función max(a,b) que tome como argumento dos números y devuelva el mayor de ellos.

1.a NO negativos
1.b Simetria
1.c input a,b
'''

def mi_max(a,b):
    if abs(a) >= 0 and abs(b)>=0:
        if a-b == 0:
            return print("a y b son iguales")
        elif a-b > 1:
            return a
        else:
            return b
    else:
        return print("No Negativos")

li = input("enter a,b ->").split(',')
le = [int(i) for i in li]
if len(li) > 2:
    print("ok",max(li))
else:
    a,b= le[0],le[1]
    print(f"a = {a} , b = {b} numero mayor: ",mi_max(a,b))



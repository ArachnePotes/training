'''
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros
y 
muestre por pantalla la <n> entre <m> da un cociente <c>
y 
un resto <r> donde <n> y <m> son los números introducidos por el usuario,
y <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''

a= input("Hey mark Aprendi a dividir, dame 2 numeros en la forma  a,b: " ).split(',')
a,b = int(a[0]),int(a[1])
print(f'cociente {a//b} resto {a%b}')

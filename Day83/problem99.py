'''
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros)
, calcule el índice de masa corporal y lo almacene en una variable,
y muestre por pantalla la frase
" Tu índice de masa corporal es <imc> "
donde <imc> es el índice de masa corporal 
calculado redondeado con dos decimales.
'''
print("Vamos a calcular tu IMC")
h = float(input("cuanto mides? (M) : "))
w = float(input("cuanto pesas? (kg): "))
imc = round( w/pow(h,2),2)
print(f"Tu índice de masa corporal es {imc}")

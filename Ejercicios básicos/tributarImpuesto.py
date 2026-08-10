'''
Escribir un programa que pregunte al usuario su edad y 
sus ingresos mensuales y muestre por pantalla si el 
usuario tiene que tributar o no.
'''

edadUsuario = int(input("Ingrese su edad: "))
ingresosMensuales = int(input("Ingrese sus ingresos mensuales: "))

if edadUsuario > 16 and ingresosMensuales >= 1000000:
    print("Usted debe tributar.")
else:
    print("Usted no debe tributar.")

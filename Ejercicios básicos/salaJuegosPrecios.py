'''
Escribir un programa que calcule el precio de entrada
de los usuarios según su edad, debe preguntar su edad
y mostrar el precio de la entrada, 
si tiene menos de 4 años entra gratis,
si tiene entre 4 y 18 paga $5000 y
si es mayor de 18 paga $10000.
'''

edadUsuraio = int(input("Ingrese su edad: "))

if edadUsuraio < 4:
    print("Usted entra gratis.")
elif edadUsuraio >= 4 and edadUsuraio < 18:
    print("Usted debe abonar $5000 para entrar.")
elif edadUsuraio >= 18:
    print("Usted debe abonar $10000 para entrar.")
else:
    print("Edad invalida.")
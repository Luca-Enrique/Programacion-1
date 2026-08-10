'''
Cuenta las vocales en una palabra ingresada por el usuario.
'''

palabra = input("Ingresá una palabra: ")
contador = 0

for letra in palabra:
    if letra in "aeiouAEIOU":
        contador += 1

print(f"Tiene {contador} vocales")
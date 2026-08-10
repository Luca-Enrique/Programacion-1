'''
Invierte una palabra ingresada por el usuario.
'''

palabra = input("Ingresá una palabra: ")
invertida = ""

for letra in reversed(palabra):
    invertida += letra

print(f"Al revés: {invertida}")
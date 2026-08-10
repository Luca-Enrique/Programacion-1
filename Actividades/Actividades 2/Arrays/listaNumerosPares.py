'''
Dada la lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
creá una nueva lista solo con los números pares.
'''

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Lista original
listaNumerosPares = [] # Lista para guardar los numeros pares

# For básico
for numero in listaNumeros:
    if numero % 2 == 0:
        listaNumerosPares.append(numero) # Lo guardamos en una lista nueva

print(f"Lista original: {listaNumeros}. Lista solo con números pares: {listaNumerosPares}.") # Imrpimimos
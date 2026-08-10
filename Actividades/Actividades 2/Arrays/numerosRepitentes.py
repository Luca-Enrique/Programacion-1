'''
Dada la lista [3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 
imprimí cuántas veces se repite cada número 
(sin usar librerías externas).
'''

listaNumeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] # Lista original

# Usamos un for para recorrer la lista original
for numero in set(listaNumeros): # Usamos el set para que el for no recorra 2 veces el mismo numero
    # Imprimimos en pantalla
    print(f"El número {numero} se repite {listaNumeros.count(numero)} veces.") # usamos el count en la lista original para contar cuantas veces se repite el numero que toma el for.
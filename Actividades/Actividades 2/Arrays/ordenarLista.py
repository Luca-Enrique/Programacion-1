'''
Dada la lista [5, 2, 8, 1, 9, 3], 
ordená de mayor a menor e imprimila.
'''

listaOrdenar = [5, 2, 8, 1, 9, 3] # Lista original

# Creamos una nueva variable/Lista para guardar dentro la lista origial, dandola vuelta para que sea de mayor a menor
listaOrdenada = sorted(listaOrdenar, reverse=True)

print(f"Lista ordenada de mayor a menor: {listaOrdenada}") # Imprimimos en consola
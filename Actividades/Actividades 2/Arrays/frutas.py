'''
Creá una lista vacía, 
agregá 4 frutas con append, 
y después imprimí cuántas hay con len.
'''

listaFrutas = [] # Lista vacia

# Agregamos frutas a la lista
listaFrutas.append("Banana")
listaFrutas.append("Manzana")
listaFrutas.append("Naranja")
listaFrutas.append("Sandia")

# Guardamos en una variable la cantidad de frutas dentro de la lista
cantidadFrutas = len(listaFrutas)

# La imprimimos
print(f"Hay {cantidadFrutas} frutas.")
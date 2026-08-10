'''
Tenés esta lista de listas (matriz):

python
notas = [
    ["Ana", 8, 9, 7],
    ["Luis", 6, 5, 10],
    ["María", 9, 9, 8]
]
Imprimí el nombre de cada alumno y su promedio de notas.
'''
# Lista original
notas = [
    ["Ana", 8, 9, 7],
    ["Luis", 6, 5, 10],
    ["María", 9, 9, 8]
]

for alumno in notas: # Recorremos la matriz
    # Primero imprime el nombre agarrando la columna 0, 
    # despues tomamos las notas con un slicing sumandolas y dividiendo por 3 para calcular el promedio
    print(f"Nombre: {alumno[0]}, Promedio: {sum(alumno[1:]) / 3}")
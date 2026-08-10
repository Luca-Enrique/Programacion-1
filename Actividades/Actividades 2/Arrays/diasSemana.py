'''
Recorrí la lista ["lunes", "martes", "miércoles", "jueves", "viernes"] 
e imprimí solo los que tienen más de 6 letras.
'''

diasSemana = ["lunes", "martes", "miércoles", "jueves", "viernes"] # Lista original

# For para recorrer la lista
for dia in diasSemana:
    if len(dia) > 6: # Si tiene mas de 6 letras
        print(dia) # lo imprime
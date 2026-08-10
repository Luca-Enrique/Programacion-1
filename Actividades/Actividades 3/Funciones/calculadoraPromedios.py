'''
Escribí un programa en Python que use funciones para calcular el promedio de notas de un alumno.

El programa debe tener estas tres funciones:

pedir_notas() — pide al usuario cuántas notas quiere ingresar y las guarda en una lista. Devuelve la lista.

calcular_promedio(notas) — recibe la lista de notas y devuelve el promedio.

mostrar_resultado(promedio) — recibe el promedio y muestra un mensaje según el resultado: 
si es mayor o igual a 6 dice "Aprobado", si no dice "Desaprobado".

 

Ejemplo de salida esperada:

¿Cuántas notas querés ingresar? 3
Nota 1: 7
Nota 2: 5
Nota 3: 9
Promedio: 7.0
¡Aprobado!
'''
# Función para pedir las notas
def pedir_notas():
    notas = [] # Lista donde se guardan las notas
    cantidadNotas = int(input("¿Cuántas notas querés ingresar? "))
    for i in range(cantidadNotas):
        notas.append(float(input(f"Nota {i + 1}: "))) # Agregamos las notas a una lista
    return notas # Devolvemos la lista

# Función para calcular el promedio
def calcular_promedio(notas):
    promedio = sum(notas) / len(notas) # Calculamos el promedio
    return promedio # Devolvemos el promedio

# Función para mostrar el resultado
def mostrar_resultado(promedio):
    print(f"Promedio: {promedio}")
    
    if promedio >= 6: # Si el promedio es mayor o igual a 6
        print("¡Aprobado!")
    else: # Sino dice desaprobado
        print("Desaprobado")

# Programa principal
def main():
    notas = pedir_notas() # Pedimos las notas
    promedio = calcular_promedio(notas) # Calculamos el promedio
    mostrar_resultado(promedio) # Mostramos el resultado

main()
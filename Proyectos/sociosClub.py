'''
Crear un programa en Python para registrar socios de un club deportivo.

Crear al menos estas funciones:

mostrar_menu()
registrar_socio()
mostrar_socios()
mostrar_resumen()

El programa debe mostrar el siguiente menú:

1- Registrar socio
2- Mostrar socios
3- Mostrar resumen
4- Salir
El menú debe repetirse hasta que el usuario elija la opción “Salir”.

1. Registrar socio
Cuando el usuario elija esta opción, pedir:

nombre
edad
deporte
cuota mensual

Guardar los datos en listas.
Ejemplo:

nombres = []
edades = []
deportes = []
cuotas = []

2. Condicionales
Usar if, elif y else para:

Clasificar socios

Menor: menos de 18 años
Adulto: entre 18 y 59 años
Adulto mayor: 60 años o más
Ejemplo:

if edad < 18:
    categoria = "Menor"
elif edad < 60:
    categoria = "Adulto"
else:
    categoria = "Adulto Mayor"

Usar un while para repetir el menú principal.

Usar un contador para contar la cantidad de socios registrados.
Ejemplo:

contador_socios += 1

Usar un acumulador para sumar el total de cuotas.
Ejemplo:

total_cuotas += cuota

Mostrar todos los socios registrados.

Ejemplo:

Ana - 25 años - Natación - $15000
Luis - 17 años - Fútbol - $12000

Mostrar:

cantidad total de socios
total de cuotas
promedio de edad

Ejemplo de ejecución:

1- Registrar socio
2- Mostrar socios
3- Mostrar resumen
4- Salir

Opción: 1

Nombre: Pedro
Edad: 20
Deporte: Básquet
Cuota mensual: 18000

Socio registrado correctamente.
'''

# Función para mostrar el menú
def mostrar_menu():
    print()
    print("Bienvenido.")
    # Mostramos el menú con saltos de linea en un solo print
    print("1- Registrar socio \n2- Mostrar socios \n3- Mostrar resumen \n4- Salir")
    print()

# Función para registrar un socio
def registrar_socio(nombres, edades, categorias, deportes, cuotas):
    # Nombre
    nombre = input("Nombre: ")
    nombres.append(nombre)
    # Edad
    edad = int(input("Edad: "))
    # if para clasificar el socio
    if edad < 18:
        categorias.append("Menor")
    elif edad < 60:
        categorias.append("Adulto")
    else:
        categorias.append("Adulto Mayor")

    edades.append(edad)
    # Deporte
    deporte = input("Deporte: ")
    deportes.append(deporte)
    # Cuota mensual
    cuota = float(input("Cuota mensual: "))
    cuotas.append(cuota)
    print()

# Función para mostrar todos los socios
def mostrar_socio(nombres, edades, categorias, deportes, cuotas):
    # For que recorre la longitud de la lista nombres, que la podemos tomar como la cantidad de socios que tiene el club
    for i in range(len(nombres)):
        print(f"{nombres[i]} - {edades[i]} años - {categorias[i]} - {deportes[i]} - ${cuotas[i]}") # Imprime los datos de los socios en pantalla

# Función para mostrar el resumen
def mostrar_resumen(nombres, edades, cuotas):
    print(f"Cantidad de socios: {len(nombres)}") # Imprime la cantidad de socios, tomando la longitud de la lista nombres
    print(f"Total de cuotas: ${sum(cuotas)}") # Imprime el total de cuotas sumandolas
    print(f"Promedio de edad: {sum(edades) / len(edades)}") # Imprime el promedio de edad, primero las suma y luego las divide

# Programa principal
def main ():
    # Listas necesarias
    nombres = []
    edades = []
    deportes = []
    cuotas = []
    categorias = []
    # While infinito hasta que usemos break
    while True:
        mostrar_menu()
        opcion = int(input("Opción: "))
        print()
        if opcion == 1:
            registrar_socio(nombres, edades, categorias, deportes, cuotas)
            print("Socio registrado correctamente.")
        elif opcion == 2:
            if len(nombres) == 0:
                print("No hay socios registrados.")
            else:
                mostrar_socio(nombres, edades, categorias, deportes, cuotas)
        elif opcion == 3:
            if len(nombres) == 0:
                print("No hay socios registrados.")
            else:
                mostrar_resumen(nombres, edades, cuotas)
        elif opcion == 4:
            print("Gracias por usar el programa.")
            break

# Ejecutamos el programa
main()
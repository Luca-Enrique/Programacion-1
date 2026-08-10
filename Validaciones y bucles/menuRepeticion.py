'''
Crear un menu que se repita hasta que el usuario decida salir, el menu debe tener 4 opciones:
1. Saludar
2. Hora ficticia
3. Número aleatorio
4. Salir

El programa debe repetirse hasta que el usuario elija 4. Salir
'''
import random

while True: #Creamos un while para que el menu se repita hasta que el usuario elija salir.

    print("Menu:")
    print("1. Saludar")
    print("2. Hora ficticia")
    print("3. Número aleatorio")
    print("4. Salir")

    try: #Tenemos en cuenta errores por si el usuario ingresa un valor que no sea un número entero.
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            print("¡Hola! ¿Cómo estás?")
        elif opcion == 2:
            print("La hora ficticia es: 25:61")
        elif opcion == 3:
            print(f"El número aleatorio es: {random.randint(1, 100)}")
        elif opcion == 4:
            print("¡Hasta luego!")
            break #Si el usuario elige la opción 4, se rompe el loop y el programa termina.

        else:
            print("Error: Por favor ingrese una opción válida (1, 2, 3 o 4).")

    except ValueError:
        print("Error: Por favor ingrese un número entero para la opción.")
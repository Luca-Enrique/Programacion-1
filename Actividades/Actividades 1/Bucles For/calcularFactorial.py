'''
Solicitar un número entero positivo y calcular su factorial ($n!$).
Si el usuario ingresa un negativo, avisar el error y no calcular.
'''
contador = 1 # Generamos un contador para mostrar cuantas veces se multiplicó

# Pedimos el numero a multiplicar
factorialIngresado = int(input("Ingrese un número para calcular su factorial: "))

# Si es negativo tira Error
if factorialIngresado < 0:
    print("Error: El número que ingresaste es negativo.")

else: # Si no, empieza el for
    # Solicita la cantidad de veces a multiplicar
    cantidadVecesMultiplicar = int(input("Ingrese la cantidad de veces que quiere multiplicar su número: "))
    for i in range(1, cantidadVecesMultiplicar + 1):
        factorialIngresado *= i
        print(f"{contador}: {factorialIngresado}")
        contador += 1
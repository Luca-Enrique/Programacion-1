'''
Escribir un programa que solicite al usuario ingresar 5 numeros,
y al final mostrar cuantos son positivos, cuantos negativos y cuantos ceros se ingresaron.
'''
#Definimos las variables para guardar los numeros positivos, negativos y ceros
positivos = 0
negativos = 0
ceros = 0
contador = 0

while contador < 5: #Creamos un while para solicitar 5 numeros al usuario

    try: #Tenemos en cuenta errores por si el usuario ingresa un valor que no sea un número entero.
        numeroIngresado = int(input("Ingrese un numero entero: "))

        #if simple para sumar los números que ingrese el usuario como si fuera un contador.
        if numeroIngresado > 0:
            positivos += 1
        elif numeroIngresado < 0:
            negativos += 1
        else:
            ceros += 1

        contador += 1 #Sumamos 1 al contador para que el loop se ejecute solo 5 veces.

    except ValueError:
        print("Error: Por favor ingrese un número entero válido.")

#Imprimimos los resultados al usuario
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
print("Cantidad de ceros:", ceros)
'''
Pedirle al usuario que ingrese 3 notas, mostrar el promedio y decir si el alumno aprobó o no 
(aprobado si el promedio es mayor o igual a 6).
'''

contador = 0
suma = 0

while contador < 3: #Creamos un while para solicitar 3 notas al usuario

    try: #Tenemos en cuenta errores por si el usuario ingresa un valor que no sea un número entero.
        notaIngresada = float(input("Ingrese una nota: "))

        if notaIngresada < 0 or notaIngresada > 10:
            print("Error: Por favor ingrese una nota entre 0 y 10.")
            continue
        else:
            suma += notaIngresada #Sumamos la nota ingresada a la variable suma.    

        contador += 1 #Sumamos 1 al contador para que el loop se ejecute solo 3 veces.

    except ValueError:
        print("Error: Por favor ingrese una nota válida.")

if contador == 3:
    promedio = suma / 3
    print(f"El promedio es: {promedio}")

    if promedio >= 6:
        print("El alumno aprobó.")
    else:
        print("El alumno no aprobó.")
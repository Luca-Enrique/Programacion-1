'''
El sistema permite reintentar el PIN hasta 3 veces. 
Si acierta, entra a un menú para retirar dinero. 
No puede retirar más de lo que tiene de saldo ni superar un límite diario de $50.000. 
El programa termina cuando retira dinero con éxito o agota los intentos.
'''

# Variables
pin = "12345"
intentos = 0
saldoUsuario = 100000
limiteSaldoDiario = 0

# Bucle para ingresar el PIN
while intentos < 3:
    pinIngresado = input("Ingrese el PIN de seguridad: ")

    if pinIngresado != pin: # Si el PIN es incorrecto
        print("El PIN no es correcto.")
        intentos += 1 # Se incrementa el contador de intentos

    elif pinIngresado == pin: # Si el PIN es correcto
        while True: # Bucle para el menú
            print()
            print("Bienvenido")
            print("1. Retirar dinero")
            print("2. Salir")
            
            # Se solicita la opción del usuario
            opcion = int(input("Ingrese una opción: "))

            if opcion == 1: # Si el usuario desea retirar dinero
                print()
                print(f"Su saldo es de ${saldoUsuario}") # Se muestra el saldo
                montoRetirado = int(input("Ingrese el monto a retirar: ")) # Y pedimos un monto a retirar

                if montoRetirado > saldoUsuario: # Si el monto a retirar es mayor al saldo
                    print("Saldo insuficiente.") 
                elif limiteSaldoDiario > 50000: # Si el saldo diario supera el límite
                    print("Usted alcanzó su limite diario de $50000.")
                else: # Si el monto a retirar es correcto
                    print(f"Usted retiró una cantidad de ${montoRetirado} ") # Mostramos el monto retirado
                    saldoUsuario -= montoRetirado # Restamos el monto retirado al saldo
                    limiteSaldoDiario += montoRetirado 
            elif opcion == 2: # Si el usuario desea salir
                print()
                print("Hasta luego!")
                break


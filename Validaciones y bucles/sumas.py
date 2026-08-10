'''
Pide al usuario números y muestra la suma total de los números ingresados. 
El programa termina cuando el usuario ingresa 0.
'''

total = 0

while True:
    n = int(input("Ingresá un número (0 para terminar): "))
    if n == 0:
        break
    total += n

print(f"La suma total es: {total}")
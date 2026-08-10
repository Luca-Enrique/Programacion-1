'''
Pide al usuario un número y muestra su tabla de multiplicar de ese número del 1 al 10.
'''

num = int(input("Ingresá un número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
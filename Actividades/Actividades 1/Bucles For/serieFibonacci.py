'''
Generar y mostrar los primeros N números de la sucesión de Fibonacci, 
donde cada número es la suma de los dos anteriores ($0, 1, 1, 2, 3, 5, 8...$).
'''
# Pedimos que el usuario ingrese un numero.
n = int(input("Ingrese el número de comienzo: "))

for _ in range(0, 10): # Mostramos los primeros 10 números de la secuencia.
    print(n)
    n += n 
'''
El usuario ingresa precios de productos. 
Si ingresa un precio negativo, es un error y debe ignorarlo. 
El proceso termina al ingresar 0. 
Al final, preguntar si tiene cupón de descuento; si dice "SÍ", aplicar un 10% al total y mostrar el ticket final.
'''
# Variables
precioTotal = 0.0

while True: # Bucle infinito hasta que según que condición lo paramos
    # Menú
    print("Bienvenido: ")
    print("0. Salir")
    print("1. Ingresar Precios")
    opcion = int(input("Ingrese su opción: "))
    print()
    while opcion == 1: # Si el usuario decide ingresar precios
        precioProducto = float(input("Ingrese el precio (0. Salir): ")) # Preguntamos el precio y tenemos en cuenta si quiere salir del bucle
        if precioProducto == 0: # Si el precio es 0, paramos el bucle
            break
        elif precioProducto < 0: # Para que el precio no pueda ser negativo
            print()
            print("Error: el precio no puede ser negativo.")
        else:
            precioTotal += precioProducto # Sumamos el precio al total
    if opcion == 0: # Paramos el bucle
        break

print()
tieneDescuento = input("¿Tiene cupón de descuento? (S: Si / N: No) ").lower() # Preguntamos si tiene descuento
print()

if tieneDescuento == "s": # Si tiene
    precioTotal *= 0.10 # Lo aplicamos
    print(f"El total es de ${precioTotal} con un descuento del 10%.")
elif tieneDescuento == "n": # Si no
    print(f"El total es de ${precioTotal}.") # Mostramos el precio total normal
else: # Si el usuario ingresa otra cosa
    print("Error: opción no válida.")
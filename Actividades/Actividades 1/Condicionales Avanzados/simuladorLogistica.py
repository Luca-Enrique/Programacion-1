'''
Determinar el costo de envío según el peso y el destino (Nacional/Internacional). 
Si es internacional y pesa más de 5kg, se aplica un recargo del 15% por aduana. 
Si es nacional y el costo supera los $20.000, el envío es gratis (descuento del 100% sobre el flete).
'''
# Pedimos el valor, el peso y el destino del paquete al usuario
print("Sístema de logistica: ")
valorPaquete = float(input("Ingrese el valor del paquete: "))
pesoPaquete = float(input("Ingrese el peso del paquete: "))
destinoPaquete = input("Ingrese el destino del paquete (N/I): ")

if destinoPaquete == "I" and pesoPaquete > 5: # Si el paquete es internacional y pesa mas de 5kg
    costoEnvio = valorPaquete * 0.15 # Aplicamos un 15% de recargo
    print(f"El costo de envío es: {costoEnvio}")
elif destinoPaquete == "N" and valorPaquete > 20000: # Si el paquete es nacional y el costo supera los $20.000
    print("Ofrecemos un 100% de descuento sobre el flete") 
else: # En cualquier otro caso
    print("No se aplica ningún descuento.")
'''
Un comercio ingresa 10 ventas. 
Cada venta tiene un "Tipo de Pago" (E: Efectivo, T: Tarjeta). 
Calcular el total recaudado en efectivo y cuántas ventas con tarjeta superaron los $5.000.
'''

# Inicialización de variables para el monto total y el conteo de ventas con tarjeta que superaron los $5000
montoTotal = 0
ventaTarjeta = 0

# Bucle para ingresar las ventas
for _ in range (0, 10):
    tipoPago = input("¿Con qué tipo de pago fue realizada la venta, (E: Efectivo, T: Tarjeta): ").lower()

    if tipoPago == "e": # Si es efectivo, se solicita el monto del pago y se suma al total
        montoPagado = int(input("Ingrese el monto del pago: "))
        montoTotal = montoPagado + montoTotal
    
    elif tipoPago == "t": # Si es con tarjeta, se solicita el monto del pago
        montoPagado = int(input("Ingrese el monto del pago: "))
        if montoPagado > 5000: # Se verifica si supera los $5000 para incrementar el conteo de ventas con tarjeta
            ventaTarjeta = ventaTarjeta + 1

print(f"El monto total en efectivo fue de ${montoTotal}, y hubieron {ventaTarjeta} ventas con tarjeta que superaron los $5000.")
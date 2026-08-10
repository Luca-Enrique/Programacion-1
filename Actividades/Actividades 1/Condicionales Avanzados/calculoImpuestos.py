'''
Calcular el inpuesto a pagar segun el sueldo bruto

Hasta $500.000 queda exento.
de $500.001 hasta $1.000.000: 10% sobre el exedente de $500.000
mas de $1.000.000: $50.000 + 20% sobre el exedente de $1.000.000
'''
# Solicitamos datos y variables
sueldoBruto = int(input("Ingrese su sueldo bruto: "))
exedenteSueldo = 0

# Condicionales
if sueldoBruto <= 500000: # Si el sueldo bruto es menor o igual a 500.000
    print("Usted queda exento.") 
elif sueldoBruto > 500000 and sueldoBruto <= 1000000: # Si el sueldo bruto es mayor a 500.000 y menor o igual a 1.000.000
    exedenteSueldo = sueldoBruto - 500000 # Calculamos el exedente
    exedenteSueldo = exedenteSueldo * 0.10 # Y calculamos el impuesto
    print(f"Usted debe pagar un impuesto de {exedenteSueldo}")
else: # Si el sueldo bruto es mayor a 1.000.000
    exedenteSueldo = sueldoBruto - 1000000 # Calculamos el exedente
    exedenteSueldo = exedenteSueldo * 0.20 + 50000 # Y el impuesto
    print(f"Usted debe pagar un impuesto de {exedenteSueldo}")
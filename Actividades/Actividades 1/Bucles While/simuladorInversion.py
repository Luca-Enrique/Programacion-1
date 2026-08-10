'''
Solicitar un capital inicial, una tasa de interés mensual y un capital objetivo. 
El programa debe calcular cuántos meses deben pasar para alcanzar o superar ese objetivo reinvirtiendo los intereses.
'''

# Variables para guardar el capital inicial, la tasa de interés mensual y el capital objetivo
capitalInicial = float(input("Ingrese el capital inicial: "))
interesMensualInicial = float(input("Ingrese la tasa de interés mensual: "))
capitalObjetivo = float(input("Ingrese el capital objetivo: "))
# Variables para despues imprimir en la consola
capital = capitalInicial
meses = 0

while capitalInicial < capitalObjetivo: # Mientras no se alcanze el objetivo
    interesMensual = capitalInicial * (interesMensualInicial / 100) # Calculamos el interes mensual, a la vez que dividimos el interes inicial en 100 para que sea un numero con coma
    capitalInicial += interesMensual # Sumamos el interes mensual al capital
    meses += 1 # Y por ultimo sumamos 1 a meses

# Imprimimos el resultado en la consola
print(f"Se necesitan {meses} meses para conseguir ${capitalObjetivo} con un capital inicial de ${capital} y un interes mensual de {interesMensualInicial}.")

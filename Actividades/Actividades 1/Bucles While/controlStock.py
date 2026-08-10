'''
Una fábrica produce piezas. 
El programa pide ingresar el estado de cada pieza (1: Optima, 2: Defectuosa). 
El proceso se detiene cuando se alcanzan 10 piezas óptimas 
o cuando aparecen 3 defectuosas seguidas (alerta de falla de máquina).
'''
# Variables que funcionan como contadores
piezasOptimas = 0
piezasDefectuosas = 0

while True: # Bucle infinito hasta que se decida parar por ciertas condiciones
    estadoPieza = input("Ingrese el estado de la pieza (O: Optima, D: Defectuosa) ").lower()

    # Si es óptima sumamos 1 al contador y reiniciamos el contador de defectuosas
    if estadoPieza == "o":
        piezasOptimas += 1
        piezasDefectuosas = 0
    # Si está defectuosa sumamos 1 al contador
    elif estadoPieza == "d":
        piezasDefectuosas += 1
    # Cachamos expeciones
    else:
        print("Error: Opción no valida.")
    
    # Condiciones para terminar el bucle
    # Si llega a 10
    if piezasOptimas == 10:
        print("Se alcanzaron las 10 piezas óptimas solicitadas.")
        break # Se termina
    # Y si hay 3 piezas defectuosas (solo puede llegar a este número si hay 3 seguidas)
    elif piezasDefectuosas == 3:
        print("Error: Falla de máquina.")
        break # Se termina igualmente



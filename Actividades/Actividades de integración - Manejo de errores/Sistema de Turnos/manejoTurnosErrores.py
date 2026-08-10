'''
Sistema de turnos con manejo de errores

Ampliación del sistema de turnos: ahora el usuario ingresa los datos por teclado, 
y el programa debe manejar entradas inválidas sin romperse.

Consigna

Creá una función pedir_hora() que solicite una hora en formato HH:MM. 
Usá try/except para capturar si el formato es incorrecto. 
Repetí el pedido con un bucle while hasta que el formato sea válido.

Creá registrar_turno(agenda, nombre, hora) que use raise ValueError si el nombre está vacío 
o si la hora ya está ocupada.

Creá cancelar_turno(agenda, nombre) que use raise ValueError si el paciente no existe en la agenda.

Creá mostrar_agenda(agenda) que recorra la lista con for y muestre los turnos ordenados por hora.

En el programa principal, llamá a las funciones dentro de bloques try/except 
y mostrá mensajes de error claros sin que el programa se detenga.

Errores que deben manejar: 
ValueError — nombre vacío o turno duplicado
ValueError — paciente no encontrado al cancelar
ValueError — formato de hora inválido (ej: "25:99" o "abc")

Ejemplo de salida esperada:
Ingresá la hora (HH:MM): abc 
Error: Formato inválido. Usá HH:MM (ej: 09:30).

Ingresá la hora (HH:MM): 10:00 

Turno registrado: María González a las 10:00 hs. 

Error: El nombre no puede estar vacío. 
Error: Ya existe un turno a las 10:00 hs. 

--- Agenda del día --- 
10:00 hs - María González 
11:00 hs - Juan Pérez

Error: No se encontró turno para Pedro López.
'''
# Importaciones
from datetime import datetime # Validar formato HH:MM

# Función para pedir la hora
def pedir_hora():
    while True: # LOOP infinito
        hora = input("Ingrese la hora (HH:MM): ")

        try:
            datetime.strptime(hora, "%H:%M") # Validamos el formato
            return hora # Si no hay error devolvemos la hora
        except ValueError:
            print(f"Error: Formato inválido. Usá HH:MM (ej: 09:30).")

# funcion para pedir el nombre
def pedir_nombre():
        nombre = input("Ingrese el nombre: ")
        if nombre.strip() != "": # Validamos que el nombre no este vacio, ademas de darle un formato con strip
            return nombre # Si no hay error devolvemos el nombre
        else:
            raise ValueError("El nombre no puede estar vacío.")
        
# Función para registrar un turno
def registrar_turno(agenda, nombre, hora):
    if any(t["hora"] == hora for t in agenda): # Validamos que la hora no este ocupada
        raise ValueError(f"Ya existe un turno a las {hora} hs.") # Captura el error si ya está ocupada
    agenda.append({"nombre": nombre, "hora": hora}) # Sino agrega el turno
    print(f"Turno registrado: {nombre} a las {hora} hs.") # Y lo imprime
    print()

# Función para cancelar un turno
def cancelar_turno(agenda, nombre):
    for turno in agenda: # Recorremos la agenda
        if turno["nombre"] == nombre: # Si el nombre coincide
            agenda.remove(turno) # Eliminamos el turno
            print(f"Turno de {nombre} cancelado.")
            print()
            return
    raise ValueError(f"No se encontró turno para {nombre}.") # Captura el error si no lo encuentra

# Función para mostrar la agenda
def mostrar_agenda(agenda):
    print("--- Agenda del día ---")
    for turno in sorted(agenda, key=lambda t: t["hora"]): # Ordenamos la agenda por hora con sorted y lambda
        print(f"{turno['hora']} hs - {turno['nombre']}") # E imprimimos el resultado

def main():
    agenda = [] # Creamos la agenda
    while True: # LOOP infinito
        try:
            print("--- Menu ---")
            print("1. Registrar turno \n2. Cancelar turno \n3. Mostrar agenda \n4. Salir")
            print("--- ---- ---")
            opcion = int(input("Ingrese una opcion: "))
            print()

            if opcion == 1:
                print("--- Registrar turno ---")
                nombre = pedir_nombre() # Pedimos el nombre
                hora = pedir_hora() # Pedimos la hora
                registrar_turno(agenda, nombre, hora) # Registramos el turno
            elif opcion == 2:
                print("--- Cancelar turno ---")
                nombre = pedir_nombre() # Pedimos el nombre
                cancelar_turno(agenda, nombre) # Cancelamos el turno
            elif opcion == 3:
                mostrar_agenda(agenda) # Mostramos la agenda
            elif opcion == 4:
                break
            else:
                print("Opcion no valida.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
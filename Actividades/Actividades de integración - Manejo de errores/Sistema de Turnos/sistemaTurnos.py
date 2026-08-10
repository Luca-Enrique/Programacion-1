'''
Sistema de turnos para un consultorio (versión completa)

Une la Actividad 1 (registrar, mostrar y cancelar turnos) con la
ampliación de manejo de errores (entrada por teclado, try/except,
raise ValueError).
'''

# Importaciones
from datetime import datetime  # Validar formato HH:MM


# Función para pedir la hora
def pedir_hora():
    while True:  # LOOP infinito
        hora = input("Ingrese la hora (HH:MM): ")
        try:
            datetime.strptime(hora, "%H:%M")  # Validamos el formato
            return hora  # Si no hay error devolvemos la hora
        except ValueError:
            print("Error: Formato inválido. Usá HH:MM (ej: 09:30).")


# Función para pedir el nombre
def pedir_nombre():
    nombre = input("Ingrese el nombre: ")
    if nombre.strip() != "":  # Validamos que el nombre no esté vacío
        return nombre.strip()
    else:
        raise ValueError("El nombre no puede estar vacío.")


# Función para registrar un turno
def registrar_turno(agenda, nombre, hora):
    if any(t["hora"] == hora for t in agenda):  # Validamos que la hora no esté ocupada
        raise ValueError(f"Ya existe un turno a las {hora} hs.")
    agenda.append({"nombre": nombre, "hora": hora})  # Agregamos el turno
    print(f"Turno registrado: {nombre} a las {hora} hs.")
    print()


# Función para cancelar un turno
def cancelar_turno(agenda, nombre):
    for turno in agenda:  # Recorremos la agenda
        if turno["nombre"] == nombre:  # Si el nombre coincide
            agenda.remove(turno)  # Eliminamos el turno
            print(f"Turno de {nombre} cancelado.")
            print()
            return
    raise ValueError(f"No se encontró turno para {nombre}.")


# Función para mostrar la agenda
def mostrar_agenda(agenda):
    if not agenda:  # Si no hay turnos cargados
        print("Agenda vacía.")
        print()
        return
    print("--- Agenda del día ---")
    for turno in sorted(agenda, key=lambda t: t["hora"]):  # Ordenada por hora
        print(f"{turno['hora']} hs - {turno['nombre']}")
    print()


# Bonus: turno más temprano (adaptado a lista de diccionarios)
def turno_mas_temprano(agenda):
    if not agenda:
        raise ValueError("No hay turnos cargados en la agenda.")
    turno = min(agenda, key=lambda t: t["hora"])  # Busca el de hora más chica
    return turno["nombre"], turno["hora"]


# Programa principal
def main():
    agenda = []  # Creamos la agenda vacía

    while True:  # LOOP infinito
        try:
            print("--- Menu ---")
            print("1. Registrar turno")
            print("2. Cancelar turno")
            print("3. Mostrar agenda")
            print("4. Ver turno más temprano")
            print("5. Salir")
            print("--- ---- ---")
            opcion = int(input("Ingrese una opcion: "))
            print()

            if opcion == 1:
                print("--- Registrar turno ---")
                nombre = pedir_nombre()
                hora = pedir_hora()
                registrar_turno(agenda, nombre, hora)
            elif opcion == 2:
                print("--- Cancelar turno ---")
                nombre = pedir_nombre()
                cancelar_turno(agenda, nombre)
            elif opcion == 3:
                mostrar_agenda(agenda)
            elif opcion == 4:
                nombre, hora = turno_mas_temprano(agenda)
                print(f"Turno más temprano: {nombre} a las {hora} hs.")
                print()
            elif opcion == 5:
                break
            else:
                print("Opcion no valida.")
                print()
        except ValueError as e:
            print(f"Error: {e}")
            print()


if __name__ == "__main__":
    main()
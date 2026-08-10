'''
Actividad 1
Sistema de turnos para un consultorio
El alumno construye un sistema básico para registrar, mostrar y cancelar turnos médicos, 
usando funciones, bucles y condicionales.

CONSIGNA
1. Creá una función registrar_turno (agenda, nombre, hora) que agregue el turno a una lista de diccionarios. 
Si ya existe un turno a esa hora, mostrá un mensaje de error con if y no lo agregues.
2. Creá una función mostrar_agenda (agenda) que recorra la lista con un bucle for y muestre cada turno.
Si la agenda está vacía, indicalo con un mensaje.
3. Creá una función cancelar_turno (agenda, nombre) que busque el turno de ese paciente con un bucle for y lo elimine. 
Si no existe, avisá con un if.
4. En el programa principal, registrá al menos 3 turnos, mostrá la agenda, cancelá uno y volvé a mostrarla.

EJEMPLO DE SALIDA ESPERADA
--- Agenda del día ---
10:00 hs - María González
11:00 hs - Juan Pérez
14:00 hs - Laura Torres

Turno de Juan Pérez cancelado.

--- Agenda actualizada ---
10:00 hs - María González
14:00 hs - Laura Torres

Bonus: Agregar una función turno_mas_temprano (agenda) que recorra la lista 
y devuelva el paciente con el horario más cercano.
'''

# funcion para registrar turnos
def registrar_turno(agenda, nombre, hora):
    if hora in agenda: # Busca si la hora ya esta ocupada
        print("Turno ocupado. Por favor, elija otra hora.")
    else: # Si no
        agenda[hora] = nombre # Agrega el turno
        print(f"Turno de {nombre} registrado para la hora {hora}.")

# funcion para mostrar la agenda
def mostrar_agenda(agenda):
    if not agenda: # Si no hay nada en la agenda
        print("Agenda vacía.")
    else: # sino 
        print("--- Agenda del día ---")
        for hora, paciente in agenda.items(): # itera sobre cada turno
            print(f"{hora} hs - {paciente}") # y lo imprime

# Funcionn para cacelar unn turno
def cancelar_turno(agenda, nombre):
    for hora, paciente in agenda.items(): # Itera sobre cada turno 
        if paciente == nombre: # Si el paciente coincide
            del agenda[hora] # Elimina el turno
            print(f"Turno de {nombre} cancelado.")
            return
    print(f"Turno de {nombre} no encontrado.") # Si despues de recorrer la agenda no lo encuetra lo avisa

# Funcion para encontrar el turno mas temprano
def turno_mas_temprano(agenda):
    horas = list(agenda.keys()) # Crea una lista con las horas
    horas.sort() # Ordena la lista
    return agenda[horas[0]] # Devuelve el primer elemento de la lista, es decir, el mas temprano

# Programa principal
def main():
    agenda = {} # Crea una agenda vacia
    # Agregamos turnos
    registrar_turno(agenda, "Maria Gonzalez", "10:00")
    registrar_turno(agenda, "Juan Perez", "11:00")
    registrar_turno(agenda, "Laura Torres", "14:00")
    # la imprimimos cancelamos, y volvemos a imprimir
    mostrar_agenda(agenda)
    cancelar_turno(agenda, "Juan Perez")
    mostrar_agenda(agenda)
    print(f"Turno mas temprano: {turno_mas_temprano(agenda)}")

# Llamamos a la funcion main para que se ejecute el programa
main()
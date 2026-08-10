'''
Un alumno aplica a una beca. Condiciones:

Debe tener un promedio >= 8 y menos de 2 inasistencias.

O bien, tener un promedio >= 9.5 independientemente de las inasistencias.

O bien, si el promedio es >= 7 pero su ingreso familiar es menor a dos salarios mínimos, se le otorga una "Beca Parcial".
'''

# Solicitamos los datos
promedioAlumno = float(input("Ingrese su promedio: "))
inasistenciasAlumno = int(input("Ingrese sus inasistencias: "))
ingresoFamiliar = float(input("Ingrese su ingreso familiar: "))

# Condicionales
if promedioAlumno >= 8 and inasistenciasAlumno < 2 or promedioAlumno >= 9.5: # Si el alumno tiene un promedio >= 8 y menos de 2 inasistencias, o si tiene un promedio >= 9.5 independientemente de las inasistencias
    print("Obtuviste una Beca.") 
elif promedioAlumno >= 7 and ingresoFamiliar < 357800: # Si el alumno tiene un promedio >= 7 pero su ingreso familiar es menor a dos salarios minimos
    print("Obtuviste una Beca parcial.")
else: # Si ninguna de las condiciones anteriores se cumple
    print("No obtuviste una beca.")
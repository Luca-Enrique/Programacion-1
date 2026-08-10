'''
Escribir un programa que lea la puntuacion del usuario
e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario
'''
#Definimos variables
puntuacionUsuario = float (input("Ingrese la puntuación del empleado: "))
dineroConseguido = 2400000 * puntuacionUsuario
rendimientoUsuario = "indefinido"

#Definimos el rendimiento del usuario en base a su puntuación
if puntuacionUsuario == 0.0:
    rendimientoUsuario = "inaceptable"
elif puntuacionUsuario == 0.4:
    rendimientoUsuario = "aceptable"
elif puntuacionUsuario >= 0.6:
    rendimientoUsuario = "meritorio"

#IF-ELSE simple para mostrar en pantalla teniendo en cuenta la puntuación
if puntuacionUsuario == 0.0 or puntuacionUsuario == 0.4 or puntuacionUsuario >= 0.6:
    print ("Su puntuación es de ", puntuacionUsuario, " este año, tu rendimiento fue ", rendimientoUsuario, " y tu recompensa es de ", dineroConseguido, " pesos." )
else:
    print("Puntuación no aceptada, ingrese los valores 0.0, 0.4, 0.6 o más.")
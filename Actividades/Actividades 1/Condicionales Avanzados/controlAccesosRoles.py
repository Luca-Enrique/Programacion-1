'''
Solicitar usuario, password y rol (Admin, Editor, Visita).

Admin: Acceso total si la clave es correcta.
Editor: Acceso solo si es día de semana (Lunes a Viernes).
Visita: Acceso solo si el usuario invitado existe en una lista predefinida.
'''

# Solicitamos usuario, contrasela y el rol.
print("Bienvenido, por favor ingrese su usuario, contraseña y rol.")
usuario = input("Usuario: ")
password = input("Contraseña: ")
rol = input("Rol (Admin, Editor, Visita): ")

# Rol Admin.
if rol.lower() == "admin" and password.lower() == "admin": # Pasamos a minuscula todo.
    print("Acceso de Admin.")

# Rol editor.
elif rol.lower() == "editor":
    diaSemana = input("Ingrese el día de la semana: ") # Pedimos dia de la semana y pasamos a minuscula.
    if diaSemana.lower() in ["lunes", "martes", "miercoles", "jueves", "viernes"]: # Comprobamos el dia de la semana.
        print("Acceso de Editor.")
    else:
        print("Acceso denegado para Editor. Solo días entre semana.")

# Rol Visita.
elif rol.lower() == "visita":
    usuariosPermitidos = ["luca", "steven"] # Lista de usuarios que pueden entrar.
    if usuario.lower() in usuariosPermitidos: # Si el usuario está en la lista.
        print("Acceso de Visita.")
    else:
        print("Acceso denegado para Visita. Usuario no invitado.")

# Rol no valido.
else:
    print("Rol no reconocido. Acceso denegado.")
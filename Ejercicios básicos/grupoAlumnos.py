'''
Escribir un programa que pregunte al usuario 
su nombre, sexo y muestre en pantalla el grupo que corresponde
'''

nombreUsuario = input("Ingrese su nombre: ")
sexoUsuario = input("Es usted Hombre o Mujer? Ingrese su respuesta: ")

if nombreUsuario <= "M" and sexoUsuario == "Mujer":
    print(nombreUsuario, ", usted pertenece al grupo A.")
elif nombreUsuario >= "N" and sexoUsuario == "Hombre":
    print(nombreUsuario, ", usted pertenece al grupo A.")
else:
    print(nombreUsuario, ", ustede pertenece al grupo B.")

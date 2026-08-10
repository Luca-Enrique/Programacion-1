'''
Pedir al usuario que ingrese una contraseña de al menos 8 caracteres, 
si no cumple volver a pedirla hasta que cumpla y 
mostrar en pantalla un mensaje que diga "Contraseña válida"
'''
#Validar que la contraseña tenga al menos 8 caracteres
contraseñaUsuario = input("Ingrese una contraseña de al menos 8 caracteres: ")

#La contraeña es valida solo si tiene una longitud de 8 caracteres o más.
while len(contraseñaUsuario) < 8:
    contraseñaUsuario = input("Contraseña inválida. Ingrese una contraseña de al menos 8 caracteres: ")
    #Si la contraseña no cumple, se repite el bolque while hasta que el usuario ingrese una contraseña válida. 

print("Contraseña válida.") #Si es valida, imprime esto enn la panntalla.

#Confirmación de la contraseña del usuario.
confirmacionContraseña = input("Por favor reingrese su contraseña para confirmarla: ") #Pedimos que la vuelva a ingresar.

#Aqui se valida, si la contraseña que volvió a ingresar no es igual a la contraseña original se repite el bloque while.
while confirmacionContraseña != contraseñaUsuario:
    confirmacionContraseña = input("Las contraseñas no coinciden, vuelva a escribirla para confirmarla: ") 
    #Pedimos que vuelva a ingresar la contraseña hasta que coincida con la contraseña original.

print("Contraseña confirmada correctamente.") 
'''
Recorrer una cadena de texto (string) con un for y determinar si es "Segura". 
Debe tener al menos 8 caracteres, contener al menos una mayúscula y al menos un número.
'''

# Solicitamos password y guardamos su longitud en una variable
password = input("Ingrese su contraseña: ")
longitudPassword = len(password)

if longitudPassword < 8:
        print("Su contraseña tiene menos de 8 caracteres.")

# Seguir en clase
'''
Escribir un programa que le pregunte al usuario su renta anual
y muestre en la consola el tipo impositivo que le corresponde
'''

usuarioRentaAnual = int(input("Ingrese el valor de su renta anual actual: "))

if usuarioRentaAnual <= 10000:
    print("Su tipo impositivo es del 5%.")
elif usuarioRentaAnual > 10000 and usuarioRentaAnual <= 20000:
    print("Su tipo impositivo es del 10%.")
elif usuarioRentaAnual > 20000 and usuarioRentaAnual <= 35000:
    print("Su tipo impositivo es del 20%.")
elif usuarioRentaAnual > 35000 and usuarioRentaAnual <= 60000:
    print("Su tipo impositivo es del 30%.")
else:
    print("Su tipo impositivo es del 45%.")
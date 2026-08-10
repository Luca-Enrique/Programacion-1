'''
Luca Enrique - Ejercicio 1

La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación:

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''

print("Bienvenido a la pizzería Bella Napoli")
tipoPizza = input("Actualmente tenemos pizzas vegetarianas y no vegetarianas. ¿Qué pizza desea? ")

if tipoPizza == "vegetariana":
    print("Ingredientes vegetarianos: Pimiento o tofu.")
    ingrediente = input("Elija un ingrediente: ")
    if ingrediente == "Pimiento" or ingrediente == "tofu":
        print("Ha elegido una pizza vegetariana con mozzarella, tomate y " + ingrediente)
    else:
        print("Ingrediente no válido.")
elif tipoPizza == "no vegetariana":
    print("Ingredientes no vegetarianos: Peperoni, Jamón o Salmón.")
    ingrediente = input("Elija un ingrediente: ")
    if ingrediente == "Peperoni" or ingrediente == "Jamón" or ingrediente == "Salmón":
        print("Ha elegido una pizza no vegetariana con mozzarella, tomate y " + ingrediente)
    else:
        print("Ingrediente no válido.")
else:
    print("Opción no válida. Por favor, responda con 'vegetariana' o 'no vegetariana'.")
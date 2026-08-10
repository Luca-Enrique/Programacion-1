'''
Actividad 2
Gestor de stock de una tienda
El alumno construye un pequeño sistema de inventario: 
puede agregar productos, consultar stock y detectar cuáles están por debajo del mínimo requerido.

CONSIGNA
1. Creá una función agregar_producto(inventario, nombre, cantidad) que agregue o actualice un producto en un diccionario. 
Si el producto ya existe, sumá la cantidad.
2. Creá una función mostrar_stock(inventario) que recorra el diccionario con un bucle for 
y muestre cada producto con su cantidad, indicando con un if si el stock es "OK" (25) o "A Bajo stock" (<5).
3. Creá una función productos_criticos (inventario, minimo) 
que devuelva una lista de los productos con stock menor al mínimo recibido como parámetro.
4. En el programa principal, cargá al menos 4 productos con distintas cantidades, 
mostrá el stock completo y luego listá los productos críticos con mínimo = 5.

EJEMPLO DE SALIDA ESPERADA
---Stock actual---

Leche : 10 unidades ✓ OK 
Pan   : 3 unidades ⚠ Bajo stock
Yogur : 7 unidades ✓ OK 
Manteca : 2 unidades ⚠ Bajo stock

Productos criticos (stock < 5): ['Pan', 'Manteca']

Bonus: Agregar una función menu() que muestre opciones numeradas 
y use un bucle while True para mantener el programa activo.
'''

# Funcion para agregar un producto
def agregar_producto(inventario, nombre, cantidad):
    if nombre in inventario: # Si el nombre del producto ya se encuentra en el inventario
        inventario[nombre] += cantidad # se le suma la cantidad
    else: # Si no
        inventario[nombre] = cantidad # se agrega con la cantidad ingresada

# Funcion para mostrar el stock
def mostrar_stock(inventario):
    for producto, cantidad in inventario.items(): # Itera sobre el inventario
        if cantidad < 5: # Si la cantidad es menor a 5
            print(f"{producto}: {cantidad} unidades ⚠ Bajo stock") # Imprime el producto y la cantidad en bajo de stock
        else: # Si no
            print(f"{producto}: {cantidad} unidades ✓ OK") # Imprime el producto y la cantidad con stock OK

# Funcion para mostrar los productos criticos
def productos_criticos(inventario, minimo):
    productos_criticos = [] # Se crea una lista para guardar los productos conn el stock inferior al minimo
    for producto, cantidad in inventario.items(): # Itera sobre el inventario
        if cantidad < minimo: # Si la cantidad es menor al minimo
            productos_criticos.append(producto) # Se agrega el producto a la lista
    return productos_criticos # Se devuelve la lista solo conn los productos criticos

# Funcion para mostrar el menu
def menu():
    inventario = {} # Se crea un diccionario para guardar el inventario
    while True: # Bucle infinito, muestra el menu
        print("1. Agregar producto")
        print("2. Mostrar stock")
        print("3. Productos criticos")
        print("4. Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese las unidades del producto: "))
            agregar_producto(inventario, nombre, cantidad)
        elif opcion == "2":
            mostrar_stock(inventario)
        elif opcion == "3":
            minimo = int(input("Ingrese el stock minimo: "))
            productos = productos_criticos(inventario, minimo)
            print(f"Productos criticos (stock < {minimo}): {productos}")
        elif opcion == "4":
            break

menu()
'''
Gestor de stock de tienda 

Une la Actividad 2 (agregar producto, mostrar stock, productos críticos)
con la ampliación de manejo de errores (entrada por teclado validada,
raise ValueError / KeyError) y agrega actualizar_stock para modificar
la cantidad de un producto ya existente.
'''

# Función para pedir una cantidad entera positiva
def pedir_cantidad(mensaje):
    while True:  # Repite hasta obtener un valor válido
        try:
            cantidad = int(input(mensaje))  # Convierte la entrada en un entero
        except ValueError:
            print("✗ Eso no es un número. Intentá de nuevo.")
            continue
        if cantidad <= 0:  # Rechaza cero y negativos
            print("✗ La cantidad debe ser mayor a cero.")
            continue
        return cantidad


# Función para agregar (o sumar stock a) un producto
def agregar_producto(inventario, nombre, cantidad):
    nombre = nombre.strip()
    if not nombre:  # Nombre vacío
        raise ValueError("El nombre del producto no puede estar vacío.")
    if nombre.isdigit():  # Nombre puramente numérico
        raise ValueError("El nombre no puede ser un número.")
    if nombre in inventario:  # Si ya existe, se suma la cantidad
        inventario[nombre] += cantidad
    else:  # Si no existe, se agrega
        inventario[nombre] = cantidad


# Función para actualizar (fijar) el stock de un producto existente
def actualizar_stock(inventario, nombre, cantidad):
    nombre = nombre.strip()
    if nombre not in inventario:  # No existe en el inventario
        raise KeyError(f"'{nombre}' no existe en el inventario.")
    inventario[nombre] = cantidad  # Se fija el nuevo valor


# Función para mostrar el stock
def mostrar_stock(inventario):
    if not inventario:  # Inventario vacío
        print("Aviso: El inventario está vacío.")
        return
    print("--- Stock actual ---")
    for producto, cantidad in inventario.items():  # Itera sobre el inventario
        if cantidad < 5:  # Bajo stock según la consigna original
            print(f"{producto}: {cantidad} unidades ⚠ Bajo stock")
        else:
            print(f"{producto}: {cantidad} unidades ✓ OK")


# Función para obtener los productos críticos
def productos_criticos(inventario, minimo):
    if minimo <= 0:  # Mínimo inválido
        raise ValueError("El mínimo debe ser mayor a cero.")
    criticos = []  # Lista de productos con stock inferior al mínimo
    for producto, cantidad in inventario.items():
        if cantidad < minimo:
            criticos.append(producto)
    return criticos


# Programa principal (menú)
def menu():
    inventario = {}  # Diccionario para guardar el inventario

    while True:  # Bucle infinito, muestra el menú
        print("--- Menu ---")
        print("1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Mostrar stock")
        print("4. Productos criticos")
        print("5. Salir\n")

        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("✗ Opcion no valida. Intenta de nuevo.\n")
            continue

        if opcion == 1:
            try:
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = pedir_cantidad("Ingrese la cantidad: ")
                agregar_producto(inventario, nombre, cantidad)
                print(f"✓ Producto agregado: {nombre.strip()} ({cantidad} unidades).\n")
            except ValueError as e:
                print(f"✗ Error: {e}\n")

        elif opcion == 2:
            try:
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = pedir_cantidad("Ingrese la cantidad: ")
                actualizar_stock(inventario, nombre, cantidad)
                print("✓ Stock actualizado.\n")
            except KeyError as e:
                print(f"✗ Error: {e}\n")

        elif opcion == 3:
            mostrar_stock(inventario)
            print()

        elif opcion == 4:
            try:
                minimo = pedir_cantidad("Ingrese el stock minimo: ")
                criticos = productos_criticos(inventario, minimo)
                print(f"Productos criticos (stock < {minimo}): {criticos}\n")
            except ValueError as e:
                print(f"✗ Error: {e}\n")

        elif opcion == 5:
            break

        else:
            print("✗ Opcion no valida. Intenta de nuevo.\n")


if __name__ == "__main__":
    menu()
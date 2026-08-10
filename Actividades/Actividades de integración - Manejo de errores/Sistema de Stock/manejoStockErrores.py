'''
Gestor de stock con manejo de errores

Ampliación del gestor de stock: el usuario carga productos desde teclado y el sistema debe resistir entradas inválidas
como cantidades negativas, texto donde va un número, o productos inexistentes.

Consigna

Creá una función pedir_cantidad(mensaje) que solicite un número entero positivo. 
Usá try/except ValueError para capturar si el usuario escribe texto, y un if para rechazar números negativos o cero. 
Repetí con while hasta obtener un valor válido.

Creá agregar_producto(inventario, nombre, cantidad) que use raise ValueError si el nombre está vacío.

Creá actualizar_stock(inventario, nombre, cantidad) que use raise KeyError si el producto no existe en el inventario.

Creá mostrar_stock(inventario) con for que indique con if si el stock es OK o bajo.

Creá productos_criticos(inventario, minimo) que use raise ValueError si el mínimo es menor o igual a cero.

En el programa principal, usá try/except para cada operación y mostrá mensajes descriptivos.

Errores que deben manejar:
ValueError — entrada no numérica o cantidad ≤ 0
ValueError — nombre de producto vacío
ValueError — mínimo inválido en productos_criticos
KeyError — producto no encontrado al actualizar

Ejemplo de salida esperada:
Ingresá la cantidad: hola 
✗ Eso no es un número. Intentá de nuevo. 

Ingresá la cantidad: -3 
✗ La cantidad debe ser mayor a cero. 

Ingresá la cantidad: 5 
✓ Producto agregado: Leche (5 unidades). 

✗ Error: El nombre del producto no puede estar vacío. 
✗ Error: 'Gaseosa' no existe en el inventario. 
✗ Error: El mínimo debe ser mayor a cero.

--- Stock actual --- 
Leche : 5 unidades ✓ OK 
Pan : 2 unidades ⚠ Bajo stock
'''

def pedir_cantidad(mensaje):
    while True: # Que se intente hasta que el usuario ingrese un valor válido
        try:
            cantidad = int(input(mensaje)) # Convierte la entrada en un entero
        except ValueError:
            print("✗ Eso no es un número. Intentá de nuevo.") # Lanza error
            continue
        if cantidad <= 0: # si es menos a 0
            print("✗ La cantidad debe ser mayor a cero.") # lanza error
            continue
        return cantidad # devuelve la cantidad

def agregar_producto(inventario, nombre, cantidad):
    nombre = nombre.strip()
    if not nombre: # devuelve false si el nombre es null (vacio)
        raise ValueError("El nombre del producto no puede estar vacío.") # lanza error
    if nombre.isdigit():  # si el nombre es puramente numérico
        raise ValueError("El nombre no puede ser un número.")
    inventario[nombre] = cantidad # agrega el producto con la cantidad ingresada

def actualizar_stock(inventario, nombre, cantidad):
    nombre = nombre.strip()
    if nombre not in inventario: # si devuelve falso = no está en el inventario
        raise KeyError(f"'{nombre}' no existe en el inventario.") # por ende lanza error
    inventario[nombre] = cantidad # y si, si está, actualiza el stock

def mostrar_stock(inventario):
    if not inventario: # si el inventario esta vacio
        print("Aviso: El inventario esta vacio.") # lanza un aviso
        return
    for producto, cantidad in inventario.items(): # Itera sobre el inventario
        if cantidad <= 3: # Si la cantidad es menor o igual a 3
            print(f"{producto}: {cantidad} unidades ⚠ Bajo stock") # Imprime el producto y la cantidad en bajo de stock
        else: # Si no
            print(f"{producto}: {cantidad} unidades ✓ OK") # Imprime el producto y la cantidad con stock OK

def productos_criticos(inventario, minimo):
    if minimo <= 0: # si el minimo es menor o igual a 0
        raise ValueError("El mínimo debe ser mayor a cero.") # lanza error
    criticos = [] # Se crea una lista para guardar los productos conn el stock inferior al minimo
    for producto, cantidad in inventario.items(): # Itera sobre el inventario
        if cantidad < minimo: # Si la cantidad es menor al minimo
            criticos.append(producto) # Se agrega el producto a la lista
    return criticos # Se devuelve la lista solo con los productos que estan con stock critico

def main():
    inventario = {} # Se crea un diccionario para guardar el inventario
    while True: # Bucle infinito, muestra el menu
        print("--- Menu ---")
        print("1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Mostrar stock")
        print("4. Productos criticos")
        print("5. Salir\n")

        try: # Tenemos en cuenta errores por si el usuario ingresa un valor que no sea un número entero.
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
    main()
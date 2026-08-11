'''
Actividad 1 - Registro y consulta de productos

El usuario puede agregar nuevos productos al stock e consultar el listado completo desde la base de datos.

CREATE TABLE producto (

id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
categoria VARCHAR(58),
precio DECIMAL (10,2),
stock INT NOT NULL
);

CONSIGNA
1. Crea una función conectar() que devuelva la conexión a la base de datos tienda.

2. Crea una función agregar producto() que:
- Pida al usuario: nombre, categoría, precio y stock
- Valide que el nombre no esté vacio y que precio y stock sean números válidos (try/except)
- Valide que precio y stock sean mayores a cero
- Inserte el producto en la tabla con INSERT usando parámetros %s
- Muestre el ID asignado por la base de datos

3. Crea una función listar_productos() que:
- Consulte todos los productos ordenados por nombre
- Los muestre en formato de tabla con columnas alineadas
- Indique con un if si el stock es "OK" (25) o "A Bajo stock" (<5)
- Si no hay productos, muestre un mensaje indicándolo

4. En el programa principal usa un menú con while True que ofrezca: agregar producto, listar productos y salir.

SALIDA ESPERADA (LISTAR)

--- Listado de productos ---

ID   Nombre       Categoria   Precio       Stock   Estado

1    Arroz        Almacén     $850.00      12      OK

2    Detergente   Limpieza    $1200.00     3       Bajo stock

3    Leche        Lácteos     $620.00      8       OK

Bonus: Agregar una opción al menú para buscar productos por categoria (SELECT con WHERE y parametros)
'''
import math
import mysql.connector
from mysql.connector import Error
from config import DB_PASSWORD, DB_USER, DB_HOST

# Función para conectar con la db
def conectar():
    try:
        return mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database='tienda')
    except Error as e:
        print(f"Error: {e}")
        return None

# Función para agregar un producto
def agregar_producto(nombre, categoria, precio, stock):
    conexion = conectar()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO producto (nombre, categoria, precio, stock) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, categoria, precio, stock))
        conexion.commit()
        print(f"Producto agregado, ID: {cursor.lastrowid}")
    except Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()

# Función para validar el agregado de un producto
def validar_y_agregar_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("Error: el nombre no puede estar vacío.")
            continue
        if len(nombre) > 100:
            print("Error: el nombre no puede superar los 100 caracteres.")
            continue
        categoria = input("Ingrese la categoría del producto: ").strip()
        if not categoria:
            print("Error: la categoría no puede estar vacía.")
            continue
        if len(categoria) > 58:
            print("Error: la categoría no puede superar los 58 caracteres.")
            continue

        try:
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
        except ValueError:
            print("Error: precio y stock deben ser números.")
            continue
        if not math.isfinite(precio) or precio <= 0 or stock <= 0:
            print("Error: precio y stock deben ser números mayores a cero.")
            continue
        break # todos los datos válidos, se sale del bucle

    agregar_producto(nombre, categoria, precio, stock)

# Función para comprobar el stock
def comprobar_stock(stock):
    if stock < 5:
        return "Bajo stock"
    return "OK"

# Función para mostrar los productos en forma de tabla
def mostrar_productos_ordenados(productos):
    print("--- Listado de productos ---")
    print(f"{'ID':<5} {'Nombre':<15} {'Categoria':<15} {'Precio':<11} {'Stock':<10} {'Estado'}")
    for id, nombre, categoria, precio, stock in productos:
        categoria = categoria if categoria is not None else "-"
        precio = precio if precio is not None else 0
        estado = comprobar_stock(stock)
        print(f"{id:<5} {nombre:<15} {categoria:<15} ${precio:<10.2f} {stock:<10} {estado}")

# Función para listar los productos
def listar_productos():
    conexion = conectar()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        sql = "SELECT id, nombre, categoria, precio, stock FROM producto ORDER BY nombre"
        cursor.execute(sql)
        productos = cursor.fetchall()
        if not productos:
            print("No hay productos en la base de datos.")
            return
        mostrar_productos_ordenados(productos)
    except Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()

# Función para buscar productos por categoria
def buscar_productos_categoria(categoria):
    conexion = conectar()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        sql = "SELECT id, nombre, categoria, precio, stock FROM producto WHERE categoria = %s"
        cursor.execute(sql, (categoria,))
        productos = cursor.fetchall()
        if not productos:
            print("No hay productos de esa categoría en la base de datos.")
            return
        mostrar_productos_ordenados(productos)
    except Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()

'''
Actividad 2 - Modificación y baja de productos

Ampliación del sistema anterior el usuario puede actualizar el precio y stock de un producto, 
o darlo de baja, siempre verificando que el ID exista antes de operar.

CONSIGNA
1. Reutiliza la función conectar() y listar_productos () de la Actividad 1.

2. Crea una función buscar_por_id(id_producto) que:
Ejecute un SELECT WHERE id=%s
Devuelva los datos del producto si existe, o None si no existe

3. Crea una función modificar_producto() que:
Pida el ID al usuario (validar que sea entero con try/except)
Use buscar por_id() para verificar que existe antes de continuar
Muestre los datos actuales del producto
Pida los nuevos valores de precio y stock
Ejecute el UPDATE y confirme con commit()
Muestre cuántas filas fueron modificadas con rowcount

4. Crea una función eliminar_producto() que:
Pida el ID al usuario (validar que sea entero)
Use buscar por_id() para verificar que existe
Pida confirmación al usuario antes de eliminar (s/h)
Ejecute el DELETE solo si el usuario confirmó

5. Integrá todo en un menú con while True que incluya las 4 operaciones: listar, agregar, modificar y eliminar.

SALIDA ESPERADA (MODIFICAR)

Ingresa el ID del producto: 2

Datos actuales:

    Nombre: Detergente
    Precio: $1200.00
    Stock: 3

Nuevo precio: 1350
Nuevo stock: 10

Producto modificado correctamente. (1 fila afectada)

Bonus: Agregar una función productos_criticos() que liste todos los productos con stock menor a 5 y muestre el
total de unidades faltantes para llegar al minimo
'''

# Función para buscar un producto por ID
def buscar_por_id(idproducto):
    conexion = conectar()
    if conexion is None:
        raise ConnectionError("No se pudo conectar a la base de datos.")
    try:
        cursor = conexion.cursor()
        sql = "SELECT id, nombre, categoria, precio, stock FROM producto WHERE id = %s"
        cursor.execute(sql, (idproducto,))
        return cursor.fetchone()
    finally:
        conexion.close()

# Función para modificar un producto
def modificar_producto():
    try:
        idproducto = int(input("Ingrese el ID del producto a modificar: "))
    except ValueError:
        print("Error: el ID debe ser un número entero.")
        return
    try:
        producto = buscar_por_id(idproducto)
    except ConnectionError:
        return
    if producto is None:
        print("Producto no encontrado.")
        return
    print("Datos actuales:")
    print(f"Nombre: {producto[1]}")
    print(f"Precio: ${producto[3]}")
    print(f"Stock: {producto[4]}")
    try:
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        nuevo_stock = int(input("Ingrese el nuevo stock: "))
    except ValueError:
        print("Error: precio y stock deben ser números.")
        return
    if not math.isfinite(nuevo_precio) or nuevo_precio <= 0 or nuevo_stock <= 0:
        print("Error: precio y stock deben ser números mayores a cero.")
        return
    conexion = conectar()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        sql = "UPDATE producto SET precio = %s, stock = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_precio, nuevo_stock, idproducto))
        conexion.commit()
        print(f"Producto modificado correctamente. ({cursor.rowcount} fila(s) afectada(s))")
    except Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()

# Función para eliminar un producto
def eliminar_producto():
    try:
        idproducto = int(input("Ingrese el ID del producto a eliminar: "))
    except ValueError:
        print("Error: el ID debe ser un número entero.")
        return
    try:
        producto = buscar_por_id(idproducto)
    except ConnectionError:
        return
    if producto is None:
        print("Producto no encontrado.")
        return
    confirmacion = input("¿Desea eliminar el producto? (s/n): ")
    if confirmacion.strip().lower() in ("s", "si", "sí"):
        conexion = conectar()
        if conexion is None:
            return
        try:
            cursor = conexion.cursor()
            sql = "DELETE FROM producto WHERE id = %s"
            cursor.execute(sql, (idproducto,))
            conexion.commit()
            print(f"Producto eliminado correctamente. ({cursor.rowcount} fila(s) afectada(s))")
        except Error as e:
            print(f"Error: {e}")
        finally:
            conexion.close()
    else:
        print("Eliminación cancelada.")

# Función para ver los productos en estado crítico
def productos_criticos():
    conexion = conectar()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        sql = "SELECT id, nombre, stock FROM producto WHERE stock < 5"
        cursor.execute(sql)
        productos = cursor.fetchall()
        if not productos:
            print("No hay productos en estado crítico.")
            return
        print("Productos críticos (stock < 5):")
        total_faltante = 0
        for id, nombre, stock in productos:
            faltante = 5 - stock
            total_faltante += faltante
            print(f"{nombre}: {stock} unidades (faltan {faltante} para el mínimo)")
        print(f"Total de unidades faltantes: {total_faltante}")
    except Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()

# Función para mostrar el menú
def menu():
    while True:
        print("--- Menú ---\n1. Agregar producto\n2. Listar productos\n3. Modificar producto\n4. Eliminar producto\n5. Buscar productos por categoría\n6. Productos críticos\n7. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            validar_y_agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            categoria = input("Ingrese la categoría a buscar: ").strip()
            buscar_productos_categoria(categoria)
        elif opcion == "6":
            productos_criticos()
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Inténtelo nuevamente.")

if __name__ == '__main__':
    menu()
        
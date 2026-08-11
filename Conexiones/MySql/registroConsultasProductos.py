'''
Actividad 1

Registro y consulta de productos

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
        return mysql.connector.connect(user='DB_USER', password='DB_PASSWORD', host='DB_HOST', database='tienda')
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

# Función para mostrar el menú
def menu():
    while True:
        print("--- Menú ---\n1. Agregar producto\n2. Listar productos\n3. Buscar productos por categoría\n4. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            validar_y_agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            categoria = input("Ingrese la categoría a buscar: ").strip()
            buscar_productos_categoria(categoria)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Inténtelo nuevamente.")

if __name__ == '__main__':
    menu()
        
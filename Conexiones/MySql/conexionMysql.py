import mysql.connector
from mysql.connector import Error
from config import DB_PASSWORD, DB_USER, DB_HOST

# Conexion con MySql
try:
    conexion = mysql.connector.connect(
        host     = 'DB_HOST',
        user     = 'DB_USER',
        password = 'DB_PASSWORD',
        database = 'biblioteca'

    )
    cursor = conexion.cursor()
    cursor.execute('SELECT VERSION()')

    print('Conectado a MySQL:', cursor.fetchone()[0])
except Error as e:
    print(f"Error: {e}")

# insertar datos
try:
    sql ='INSERT INTO autores (nombre, pais, anio_nacimiento) VALUES (%s, %s, %s)'
    datos = ('Pablo Neruda','Chile','1925-08-28')

    cursor.execute(sql, datos)
    conexion.commit()
    print('autor insertado. ID:', cursor.lastrowid)
except Error as e:
    print(f"Error: {e}")
finally:
    if cursor:
        cursor.close()
    if conexion and conexion.is_connected():
        conexion.close()
        print('Conexión cerrada.')
# Prácticas de Programación en Python

Ejercicios y proyectos de práctica en **Python 3**: actividades de clase, problemas de lógica, validación de datos, manejo de errores, conexión a bases de datos MySQL y desarrollo web básico con Flask.

## Documentación

- `INDICE.md` → Catálogo de todos los archivos del repositorio, con descripción de cada uno.
- `CHANGELOG.md` → Registro de versiones y cambios.

## Tecnologías

- Lenguaje: **Python 3**
- Editor: **Visual Studio Code**
- Librerías: `flask`, `mysql-connector-python`

## Instalación

```bash
pip install flask mysql-connector-python
```

## Configuración de MySQL

La carpeta `Conexiones/MySql/` lee las credenciales desde un archivo `.env` (excluido de Git). Para configurarlo:

1. Copiar `Conexiones/MySql/.env.example` como `Conexiones/MySql/.env`.
2. Completar `DB_HOST`, `DB_USER` y `DB_PASSWORD`.
3. Crear la base de datos `tienda` y la tabla `producto`:

   ```sql
   CREATE DATABASE tienda;
   USE tienda;

   CREATE TABLE producto (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(100) NOT NULL,
       categoria VARCHAR(58),
       precio DECIMAL(10,2),
       stock INT NOT NULL
   );
   ```

El archivo `Conexiones/MySql/config.py` carga el `.env` y expone `DB_HOST`, `DB_USER` y `DB_PASSWORD` para los scripts.

## Estructura

```
Actividades/            Unidades de clase (condicionales, bucles, arrays, funciones, manejo de errores)
Conexiones/MySql/       Conexión y gestión de datos con MySQL
Ejercicios básicos/     Programas sueltos de lógica
Validaciones y bucles/  Menús interactivos, validación de entrada y bucles
Proyectos/              Proyectos completos en consola (ej: Blackjack)
Fundamentos Web/        HTML, CSS, maquetación y aplicaciones con Flask
```

El detalle archivo por archivo está en `INDICE.md`.

## Notas

Estos ejercicios forman parte del proceso de aprendizaje y pueden contener diferentes versiones o mejoras a medida que se adquiere más experiencia.

**Última actualización:** 18 Septiembre 2026
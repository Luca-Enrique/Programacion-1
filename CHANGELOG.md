# Changelog
---

## [v1.3.0] - 2026-08-11

#### Features

- Agrego la Actividad 2 en `registroConsultasProductos.py`: funciones `buscar_por_id()`, `modificar_producto()` y `eliminar_producto()` con validación del ID y confirmación antes de eliminar
- Agrego el bonus `productos_criticos()` que lista los productos con stock menor a 5 y el total de unidades faltantes
- Separo las credenciales de MySQL en `config.py` (en la misma carpeta del script y excluido de Git)

#### Fixes

- Corrijo el manejo de columnas `NULL` en el listado de productos (evita `TypeError`)
- Corrijo la validación del precio para rechazar valores `nan`/`inf`
- Agrego validaciones de entero y de precio/stock mayores a cero en modificar y eliminar producto
- Agrego la muestra de `rowcount` al modificar y eliminar

#### Docs

- Actualizo `README.md` con la nueva funcionalidad y la configuración de `config.py`

---

## [v1.2.0] - 2026-08-11

#### Features

- Agrego `registroConsultasProductos.py` en Conexiones → MySql: menú interactivo para registrar y listar productos, con validación de datos, estado de stock y búsqueda por categoría

#### Docs

- Actualizo `README.md` con la nueva actividad y una sección de configuración de MySQL (conector, creación de la base `tienda` y la tabla `producto`)

---

## [v1.1.0] - 2026-08-09

#### Features

- Agrego `analisisTemperaturas.py` y `validarFortalezaPassword.py` en Actividades 1 → Bucles For
- Agrego `procesadorCompras.py` y `validarDatosReentrada.py` en Actividades 1 → Bucles While
- Agrego `calculadoraPromedios.py` en Actividades 3 → Funciones
- Agrego Actividades de integración - Manejo de errores (Sistema de Stock y Sistema de Turnos)
- Agrego `conexionMysql.py` en Conexiones → MySql
- Agrego Mi Web (`App.py`, `templates/index.html`, `static/estilos.css`)
- Agrego `sociosClub.py` en Proyectos

#### Fixes

- Corrijo nombres de archivos en `README.md` (`serieFibonacci.py` y `controlAccesosRoles.py`)

#### Docs

- Actualizo `README.md` con nuevas secciones y tecnologías (`flask`, `mysql-connector-python`)
- Creo `CHANGELOG.md` con este registro de cambios

---

## [v1.0.0] - 2026-06-29

#### Features

- Agrego contenido inicial de la carpeta: Actividades 1 y 2, Ejercicios básicos, Validaciones y bucles y Proyectos (`blackJack.py`)

#### Docs

- Creo `README.md` con la documentación base de la carpeta

---

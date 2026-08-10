# Prácticas de Programación en Python

En esta carpeta se encuentran actividades de práctica realizadas en Python.

Los ejercicios incluyen:

- Actividades propuestas por el profesor
- Ejercicios realizados de forma autodidacta
- Pruebas de lógica y resolución de problemas

## Objetivo

El objetivo de esta carpeta es desarrollar habilidades en programación mediante la práctica constante, reforzando conceptos fundamentales como:

- Condicionales (`if`, `elif`, `else`)
- Bucles (`while`, `for`)
- Validación de datos
- Manejo de errores (`try`, `except`, `raise`)
- Contadores y acumuladores
- Uso de funciones
- Listas y matrices
- Diccionarios
- Lógica de resolución de problemas
- Conexión a bases de datos (MySQL)
- Desarrollo web básico (Flask)

## Progreso

A medida que avanzo en el aprendizaje, los ejercicios se vuelven más complejos.  
Actualmente se incluyen:

- Ejercicios básicos de lógica
- Programas con validación de datos
- Menús interactivos
- Uso de listas y matrices
- Funciones
- Manejo de errores (`try`, `except`, `raise`)
- Proyectos completos en consola (ej: Blackjack)
- Actividades de clase
- Conexión a bases de datos MySQL
- Aplicaciones web básicas con Flask

## Tecnologías utilizadas

- Lenguaje: **Python 3**
- Editor: **Visual Studio Code**
- Librerías utilizadas:
  - `random`
  - `flask`
  - `mysql-connector-python`

## Contenido

- `README.md` → Documento descriptivo de la carpeta y su contenido.
- `CHANGELOG.md` → Registro de cambios y versiones de los proyectos.

### Actividades 1

- Primeras actividades dadas en clase.

#### Condicionales Avanzados

- `calculoImpuestos.py` → Calcula el impuesto a pagar según el sueldo bruto utilizando tramos progresivos.
- `validacionTriangulo.py` → Determina si tres longitudes forman un triángulo y lo clasifica según sus ángulos.
- `aplicarBecas.py` → Determina si un alumno obtiene una beca completa o parcial según su promedio, inasistencias e ingresos.
- `simuladorLogistica.py` → Calcula el costo de envío según el peso, destino y posibles recargos o descuentos.
- `controlAccesosRoles.py` → Simula un sistema de acceso según usuario, contraseña y rol con distintas reglas.

#### Bucles For

- `procesamientoVentas.py` → Procesa 10 ventas, calculando el total recaudado en efectivo y contando las ventas con tarjeta que superaron los $5.000.
- `calcularFactorial.py` → Calcula el factorial de un número ingresado por el usuario.
- `serieFibonacci.py` → Genera la serie de Fibonacci hasta un número límite ingresado por el usuario.
- `analisisTemperaturas.py` → Analiza las temperaturas máximas de los últimos 7 días, informando el promedio semanal, cuántos días superaron los 30 °C y en qué día se registró la temperatura más baja.
- `validarFortalezaPassword.py` → Recorre una contraseña y determina si es "segura" según su longitud, presencia de mayúsculas y números.

#### Bucles While

- `cajeroAutomatico.py` → Simula un cajero automático con opciones de retiro.
- `controlStock.py` → Simula un control de maquinaria, determinando productos defectuosos o óptimos, si hay mas de 3 defectuosos detiene la producción.
- `simuladorInversion.py` → Simula una inversión con interés compuesto, calculando el monto final hasta que alcance un objetivo, mostrando cuantos meses se necesitan.
- `procesadorCompras.py` → Registra precios de productos, ignora precios negativos y, al terminar, aplica un descuento del 10% si el usuario tiene cupón, mostrando el ticket final.
- `validarDatosReentrada.py` → Valida un formulario de nombre, edad y email, informando el error específico y repidiendo solo el dato inválido.

### Actividades 2

#### Arrays

- `diasSemana.py` → Recorre una lista de días de la semana e imprime solo los que tienen más de 6 letras.
- `frutas.py` → Crea una lista de frutas utilizando `append` y muestra cuántos elementos contiene.
- `listaNumerosPares.py` → Genera una nueva lista con los números pares de una lista original.
- `listaSlicing.py` → Utiliza slicing para obtener los elementos del medio de una lista.
- `matrizNotasAlumnos.py` → Recorre una matriz de alumnos y calcula el promedio de notas de cada uno.
- `nombres.py` → Muestra el primer y el último elemento de una lista de nombres.
- `numerosRepitentes.py` → Cuenta cuántas veces se repite cada número dentro de una lista.
- `ordenarLista.py` → Ordena una lista numérica de mayor a menor utilizando `sorted`.

### Actividades 3

#### Funciones

- `calculadoraPromedios.py` → Usa funciones para pedir notas, calcular el promedio y mostrar si el alumno aprobó o desaprobó.

### Actividades de integración - Manejo de errores

Prácticas que combinan proyectos previos con validación de datos y manejo de errores mediante `try`, `except`, `raise ValueError` y `raise KeyError`.

#### Sistema de Stock

- `stockTienda.py` → Gestor de stock de una tienda: agrega productos, muestra el stock completo y detecta los productos críticos.
- `manejoStockErrores.py` → Ampliación del gestor de stock que resiste entradas inválidas (cantidades negativas, texto donde va un número o productos inexistentes).
- `sistemaStock.py` → Versión completa que une el gestor de stock con el manejo de errores y agrega la función `actualizar_stock`.

#### Sistema de Turnos

- `turnosMedicos.py` → Sistema básico para registrar, mostrar y cancelar turnos médicos de un consultorio.
- `manejoTurnosErrores.py` → Ampliación del sistema de turnos que valida la hora en formato HH:MM y maneja entradas inválidas sin romperse.
- `sistemaTurnos.py` → Versión completa que une el sistema de turnos con la validación de hora y el manejo de errores.

### Ejercicios básicos

- `grupoAlumnos.py` → Programa que asigna a los alumnos a un grupo (A o B) según su nombre y sexo.
- `numerosPares.py` → Programa que determina si un número ingresado es par o impar.
- `pizzeriaMenu.py` → Programa que muestra un menú de pizzas y permite elegir ingredientes según si la pizza es vegetariana o no.
- `puntuacionEmpresa.py` → Programa que calcula el nivel de rendimiento de un empleado y su recompensa según su puntuación.
- `salaJuegosPrecios.py` → Programa que calcula el precio de entrada a una sala de juegos según la edad del usuario.
- `tramoImpositivo.py` → Programa que determina el tipo impositivo correspondiente según la renta anual ingresada.
- `tributarImpuesto.py` → Programa que indica si un usuario debe tributar según su edad e ingresos mensuales.

### Validaciones y bucles

- `menuRepeticion.py` → Implementa un menú interactivo que se repite hasta que el usuario decide salir.
- `promedioNotas.py` → Solicita 3 notas, calcula el promedio y determina si el alumno aprobó.
- `validacionNumeros.py` → Programa que solicita varios números y cuenta cuántos son positivos, negativos o cero.
- `validarContrasena.py` → Programa que valida que una contraseña cumpla con una longitud mínima y confirma su ingreso.
- `contadorVocales.py` → Cuenta la cantidad de vocales en una palabra ingresada por el usuario.
- `invertirPalabras.py` → Invierte una palabra ingresada por el usuario.
- `sumas.py` → Suma números ingresados por el usuario hasta que se ingresa 0.
- `tablaMultiplicar.py` → Muestra la tabla de multiplicar de un número del 1 al 10.

### Proyectos

- `blackJack.py` → Simula un juego básico de Blackjack en consola con sistema de apuestas y saldo.
- `sociosClub.py` → Programa para registrar socios de un club deportivo con menú interactivo, funciones y resumen de datos.

### Conexiones

#### MySql

- `conexionMysql.py` → Conecta a una base de datos MySQL local, consulta la versión del servidor e inserta un autor en la tabla `autores`.

### Mi Web

Aplicación web básica desarrollada con Flask.

- `App.py` → Servidor Flask que renderiza una plantilla HTML en la página de inicio.
- `templates/index.html` → Plantilla HTML de la página principal.
- `static/estilos.css` → Hoja de estilos de la página.

## Notas

Estos ejercicios forman parte del proceso de aprendizaje y pueden contener diferentes versiones o mejoras a medida que se adquiere más experiencia.

**Última actualización:** 9 Agosto 2026

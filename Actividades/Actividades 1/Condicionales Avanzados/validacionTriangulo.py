'''
Solicitar tres longitudes. 
Primero, determinar si pueden formar un triángulo (la suma de dos lados siempre debe ser mayor al tercero). 
Si es válido, clasificarlo por sus lados y por sus ángulos (rectángulo, acutángulo u obtusángulo) 
usando el Teorema de Pitágoras ($a^2 + b^2 = c^2$).
'''

# Damos la bienvenida y solicitamos las 3 longitudes
print("Bienvenido, ingrese 3 longitudes.")
a = int(input("Ingrese la primera: "))
b = int(input("Ingrese la segunda: "))
c = int(input("Ingrese la tercera: "))

# Acomodamos los lados de mayor a menor
lados = sorted([a, b, c])
a, b, c = lados

if a + b > c: # If para comprobar que sea un triángulo
    trianguloClasificacion = "" # Creamos una variable para posteriormente imprimir su clasificación

    if a **2 + b **2 == c **2: 
        trianguloClasificacion = "rectángulo." # Es un rectangulo
    elif a **2 + b **2 > c **2:
        trianguloClasificacion = "acutángulo." # Es un acutángulo
    elif a **2 + b **2 < c **2:
        trianguloClasificacion = "obtusángulo." # Es un obtusángulo
    else: 
        trianguloClasificacion = "sin clasificación."

    print(f"Usted ingresó un triángulo {trianguloClasificacion}")
else:
    print("Usted ingresó longitudes las cuales no forman un triángulo.")
        
    
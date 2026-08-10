"""
Desarrollar un programa en Python que simule un juego básico de Blackjack en consola entre el usuario y la computadora (dealer).
El programa debe cumplir con las siguientes condiciones:

El objetivo del juego es acercarse lo más posible a 21 sin pasarse.

Al comenzar el juego:

- El jugador recibe 2 cartas aleatorias.
- El dealer recibe 2 cartas aleatorias (una puede permanecer oculta).

Las cartas deben tener los siguientes valores:

- Cartas del 2 al 10 → valen su número.
- J, Q y K → valen 10.
- A (As) → vale 11, pero si el total supera 21, puede contar como 1.

Durante su turno, el jugador podrá elegir:

1 - Pedir carta (Hit)
2 - Plantarse (Stand)

Si el jugador pide carta:

- Se le debe asignar una nueva carta aleatoria.
- Se debe mostrar el total actualizado.
- Si el total supera 21, el jugador pierde automáticamente.

Cuando el jugador se planta:

- El dealer debe pedir cartas automáticamente hasta alcanzar al menos 17 puntos.

Al finalizar:

El programa debe mostrar:

- Las cartas del jugador.
- Las cartas del dealer.
- El total de cada uno.
- Quién ganó la partida.
- Debe finalizar cuando el jugador decida no jugar o cuando se quede sin saldo.

Condiciones de victoria:

- Si el jugador supera 21 → pierde.
- Si el dealer supera 21 → gana el jugador.
- Si ninguno se pasa → gana el que tenga mayor puntaje.
- Si ambos tienen el mismo puntaje → empate.

Apuestas:
- El jugador comienza con un saldo inicial de $1000.
- Antes de cada partida, el jugador debe apostar una cantidad de su saldo.
- El jugador puede elegir apostar las cantidades de 5, 10, 20, 50, 100, 500 o 1000, o también puede elegir "ALL IN" para apostar todo su saldo.
- Si el jugador apuesta mas dinero del que tiene, el programa debe mostrar un mensaje de error y solicitar una nueva apuesta.
- Si el jugador gana, se le suma a su saldo la cantidad apostada.
- Si el jugador pierde, se le resta a su saldo la cantidad apostada.
- Si el jugador empata, su saldo no cambia.
"""

import random

def valor_carta(carta): #Función para asignar el valor a cada carta según las reglas del Blackjack.
    if carta in ['J', 'Q', 'K']: 
        return 10
    elif carta == 'A':
        return 11
    else:
        return int(carta)

def total_mano(mano): #Función para calcular el total de una mano, teniendo en cuenta el valor de las cartas y ajustando el valor del As si es necesario.
    total = sum(valor_carta(carta) for carta in mano)
    # Ajustar el valor del As si el total supera 21
    ases = mano.count('A')
    while total > 21 and ases > 0:
        total -= 10
        ases -= 1
    return total

def mostrar_manos(mano_jugador, mano_dealer, ocultar_carta=True): #Función para mostrar las manos del jugador y el dealer.
    print(f"Mano del jugador: {mano_jugador} (Total: {total_mano(mano_jugador)})")
    if ocultar_carta: #Si ocultar_carta es True, se muestra solo la primera carta del dealer y se oculta la segunda.
        print(f"Mano del dealer: [{mano_dealer[0]}, '?']")
    else:
        print(f"Mano del dealer: {mano_dealer} (Total: {total_mano(mano_dealer)})")

def solicitar_apuesta(saldo):
    while True:
        apuesta = input(f"Ingresa tu apuesta (5, 10, 20, 50, 100, 500, 1000 o ALL IN): ")
        if apuesta.upper() == "ALL IN":
            return saldo
        elif apuesta in ['5', '10', '20', '50', '100', '500', '1000']:
            apuesta = int(apuesta)
            if apuesta > saldo:
                print("Error: No puedes apostar más de tu saldo. Intenta nuevamente.")
            else:
                return apuesta
        else:
            print("Error: Apuesta no válida. Por favor ingresa una cantidad válida o ALL IN.")

def jugar_blackjack(apuesta):
    # Crear un mazo estándar de 52 cartas (4 palos por cada valor)
    cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(cartas)

    def repartir_carta(mazo):
        return mazo.pop()

    jugador = [repartir_carta(cartas), repartir_carta(cartas)]
    dealer = [repartir_carta(cartas), repartir_carta(cartas)]

    mostrar_manos(jugador, dealer)

    while True:
        opcion = input("¿Desea pedir carta (1) o plantarse (2)? ")
        if opcion == '1':
            jugador.append(repartir_carta(cartas))
            mostrar_manos(jugador, dealer)
            if total_mano(jugador) > 21:
                print("¡Has superado 21! ¡Pierdes!")
                return "pierde", jugador, dealer
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")

    while total_mano(dealer) < 17:
        dealer.append(repartir_carta(cartas))

    mostrar_manos(jugador, dealer, ocultar_carta=False)

    total_jugador = total_mano(jugador)
    total_dealer = total_mano(dealer)

    if total_dealer > 21:
        print("¡El dealer ha superado 21! ¡Ganas!")
        return "gana", jugador, dealer
    elif total_jugador > total_dealer:
        print("¡Ganas!")
        return "gana", jugador, dealer
    elif total_jugador < total_dealer:
        print("¡Pierdes!")
        return "pierde", jugador, dealer
    else:
        print("¡Empate!")
        return "empate", jugador, dealer

def main():
    saldo = 1000
    print("¡Bienvenido al juego de Blackjack!")
    while saldo > 0:
        print(f"\nTu saldo actual es: ${saldo}")
        apuesta = solicitar_apuesta(saldo)
        resultado, mano_jugador, mano_dealer = jugar_blackjack(apuesta)
        if resultado == "gana":
            saldo += apuesta
            print(f"¡Ganaste la apuesta! Saldo: ${saldo}")
        elif resultado == "pierde":
            saldo -= apuesta
            print(f"Perdiste la apuesta. Saldo: ${saldo}")
            if saldo == 0:
                print("Te has quedado sin saldo. ¡Juego terminado!")
                break
        else:
            print(f"Empate. Tu saldo permanece en: ${saldo}")
        if saldo == 0:
            print("Te has quedado sin saldo. ¡Juego terminado!")
            break
        reiniciar = input("¿Desea jugar nuevamente? (s/n) ")
        if reiniciar.lower() != 's':
            print("¡Gracias por jugar! ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
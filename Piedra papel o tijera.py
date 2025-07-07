import random
print("Bienvenido al juego Piedra, Papel o Tijera")

jugar = "si"

while jugar == "si":
    print("\nEscribe: piedra, papel o tijera")
    opciones = ["piedra", "papel", "tijera"]
    jugador = input("Tu jugada: ")

    if jugador == "piedra" or jugador == "papel" or jugador == "tijera":

        computadora = random.choice(opciones)

        print("La computadora eligió:", computadora)

        if jugador == computadora:
            print("Empate")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("Perdiste :(")

    else:
        print("Opción inválida. Debes escribir piedra, papel o tijera.")

    print("\n¿Quieres jugar de nuevo? (si/no)")
    jugar = input("Escribe tu respuesta: ") 
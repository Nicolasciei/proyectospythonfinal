from random import randint

respuesta = "s"
while respuesta == "s":
    print("*" *55)
    print("        piedra,papel o tigera")
    print("*" * 55)
    jugador = input("Escribir tu jugada: piedra, papel o tijera: ")

    eleccion = ["piedra", "papel", "tijera"]
    computadora = eleccion[randint(0, 2)]
    print("La computadora elige: ", computadora)

    if computadora == jugador:
        print("Hay un empate")
    elif computadora == "piedra" and jugador == "tijera":
        print("La computadora gana. La pidra le gana a tijera")
    elif computadora == "papel" and jugador == "tijera":
        print("El jugador gana. La tijera le gana al papel")
    elif computadora == "tijera" and jugador == "piedra":
        print("El jugador gana. La piedra le gana a tijera")
    elif computadora == "papel" and jugador == "piedra":
        print("La computadora gana. El papel le gana a la piedra")
    elif computadora == "piedra" and jugador == "papel":
        print("El jugador gana. El papel le gana a la piedra")
    print("Desea continuar? si(s) No(n)")
    respuesta = input()




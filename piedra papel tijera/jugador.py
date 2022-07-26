from random import randint

jugador = input("escribir tu jugada:piedra,papel , tigera:")

eleccion = ["piedra","papel","tijera"]
computadora =eleccion[randint(0,2)]
print("la computadora elige:", computadora)

if computadora == jugador:
    print("hay un empate")
elif computadora == "piedra" and jugador == "tigera":
    print("la computadora gana. La piedra le gana a tigera")



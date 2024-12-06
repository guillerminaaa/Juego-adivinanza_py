from ast import Break
import random


secret_number = random.randint(0, 100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvendido al juego de adivinar el numero secreto !!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("GAME OVER")
        Break
    entrada = input("introduce un numero del 1 al 99: ")
    numero = int(entrada)

    if numero == secret_number:
        print("Felicidades has adivinado el numero secreto!!")
        adivinado = True
    elif numero < secret_number:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")

    cant_intentos = cant_intentos + 1

#https://replit.com/join/dsxsjqzqgh-azul-esmeraldae

# Desarrolla un programa que simule un juego de rol simple. Los jugadores deben elegir entre diferentes personajes y luego enfrentar desafios que involucran lazar dados para determinar el éxito o el fracaso. Usa condicionales y operadores lógicos para determinar los resultados de las acciones de los jugadores.

import random

def lanzar_dado():
    return random.randint(1, 6)

def elegir_personaje():
    print("Elige tu personaje:")
    print("1. Hada")
    print("2. Sirena")
    print("3. Rey")
    opcion = int(input("Ingresa el número de tu elección: "))

    if opcion == 1:
        return "Hada"
    elif opcion == 2:
        return "Sirena"
    elif opcion == 3:
        return "Rey/reina"
    else:
        print("Opción inválida. Serás un Rey/reina")
        return "Rey"


def enfrentar_desafio(personaje):
    dificultad = lanzar_dado()
    exito = lanzar_dado()

    if personaje == "Hada":
        exito += 2
    elif personaje == "Sirena":
        exito += 1
    elif personaje == "Rey/Reina":
        exito += 3

    if exito >= dificultad:
        print("¡Has tenido éxito en el desafío!")
    else:
        print("Has fallado en el desafío. ¡Mejor suerte la próxima vez!")

print("Bienvenido al juego de rol simple.")
jugador = elegir_personaje()
print(f"Eres un {jugador}.")

while True:
    print("\nNo quieres enfrentar un desafío (presiona 'S' para salir):")
    accion = input("Presiona Enter para lanzar el dado...")

    if accion.lower() == 'S':
        print("Gracias por jugar!!!")
        break

    enfrentar_desafio(jugador)

if personaje == "Hada":
    exito += 2
elif personaje == "Sirena":
    exito += 1
elif personaje == "Rey/Reina":
    exito += 3

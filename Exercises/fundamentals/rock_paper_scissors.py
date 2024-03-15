# Juego de piedra, papel o tijera

# Desarrollar una versión del clásico juego de piedra, papel o tijeras, donde el usuario juega contra la computadora. El programa debe pedir al usuario su elección, generar una elección para la computadora y determinar el ganador.

import random

def obtener_eleccion_computadora():
    opciones = ['piedra', 'papel', 'tijeras']
    eleccion_computadora = random.choice(opciones)
    return eleccion_computadora

def determinar_ganador(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        return "Empate"
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_usuario == 'tijeras' and eleccion_computadora == 'papel'):
        return "¡Ganaste!"
    else:
        return "¡La computadora ganó!"

def main():
    print("Bienvenido al juego de piedra, papel o tijeras.")

    eleccion_usuario = input("Elige tu jugada (piedra, papel o tijeras): ").lower()
    if eleccion_usuario not in ['piedra', 'papel', 'tijeras']:
        print("Elección inválida. Por favor, elige piedra, papel o tijeras.")
        return

    eleccion_computadora = obtener_eleccion_computadora()

    print(f"La computadora eligió: {eleccion_computadora}")

    resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
    print(resultado)

if __name__ == "__main__":
    main()

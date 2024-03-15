# Adivina el número

# Implementar un juego donde el usuario intenta adivinar un número generado por la computadora, y otra variante donde la computadora intenta adivinar un número pensado por el usuario.

import random

def jugar_usuario_adivina():
    print("Bienvenido al juego de adivinar números. Tienes que adivinar el número entre 1 y 100.")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("Introduce tu suposición: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

def jugar_computadora_adivina():
    print("Piensa en un número entre 1 y 100, y yo intentaré adivinarlo.")
    input("Presiona Enter cuando estés listo...")

    limite_inferior = 1
    limite_superior = 100
    intentos = 0

    while True:
        intento = random.randint(limite_inferior, limite_superior)
        print(f"¿Es {intento} tu número?")

        respuesta = input("Ingresa 's' si es demasiado bajo, 'a' si es demasiado alto, o 'c' si es correcto: ").lower()
        intentos += 1

        if respuesta == 'c':
            print(f"¡Genial! Adiviné tu número en {intentos} intentos.")
            break
        elif respuesta == 's':
            limite_inferior = intento + 1
        elif respuesta == 'a':
            limite_superior = intento - 1
        else:
            print("Respuesta inválida. Por favor, ingresa 's', 'a' o 'c'.")

def main():
    print("Bienvenido al juego de adivinar números.")
    opcion = input("Elige una opción:\n1. Adivina el número (Usuario adivina)\n2. Adivina el número (Computadora adivina)\n")

    if opcion == '1':
        jugar_usuario_adivina()
    elif opcion == '2':
        jugar_computadora_adivina()
    else:
        print("Opción inválida. Por favor, selecciona 1 o 2.")

if __name__ == "__main__":
    main()

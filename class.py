import random

juego = []

# Ciclo del juego en general
while True:
    print("¡Bienvenidos a mi CASINO!")

    jugador = random.randint(2, 26) #Número entero aleatorio entre 2 y 26
    dealer = random.randint(2, 26)
    
    print(f"El jugador tiene {jugador} cartas \nEl dealer tiene {dealer} cartas")

    # Ciclo de la partida
    while True:
        quiere_mas_cartas = input("¿Desea otra carta? (s/n): ")
        if quiere_mas_cartas == 's':
            jugador += random.randint(1, 13)

            print(f"Ahora el jugador tiene {jugador} cartas \nEl dealer tiene {dealer} cartas")
        else:
            if jugador == 21 or (jugador > dealer and jugador < 21):
                print("¡GANASTE! :)")
                juego.append("jugador")
                break
            elif jugador == dealer:
                print("¡PERDISTE! Ganó el Dealear :(")
                juego.append("dealer")
                break
            else:
                print("¡PERDISTE! Ganó el Dealear :(")
                juego.append("dealer")
                break

    preguntar_si_salir = input("¿Desea continuar? (s/n): ")

    if preguntar_si_salir == 'n':
        print("Vuelve pronto :)")
        break
    else:
        print("\n" * 20)

print(juego)
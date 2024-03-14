# Calculadora de Factorial

# Crear un programa que calcule el factorial de un número ingresado por el usuario. Utilizar tanto un ciclo for como un ciclo while para realizar el cálculo.

while True:
    number = int(input("Ingrese el número el cuál quiere saber el factorial: "))

    result = number

    for i in range(1, number):
        result *= i

    print(f"El factorial de {number} es: {result}")

    response = input("¿Deseas calcular otro número? (s/n): ")

    if response == 'n':
        print("Vuelve pronto :)")
        break
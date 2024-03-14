# Calculadora de IMC

# Crear un programa que calcule el índice de Masa Corporal (IMC) a partir del peso (en kilogramos) y la altura (en metros) ingresados por el usuario.

height = input("Ingrese su altura en metros: ")
height = float(height)

weight = float(input("Ingrese su peso en kilogramos: "))

IMC = weight / (height ** 2)
print(f"El valor del IMC es: {IMC}")
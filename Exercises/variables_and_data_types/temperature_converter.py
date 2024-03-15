# Conversor de Temperatura

# Escribir un programa que convierta la temperatura de grados Celsius a Fahrenheit y viceversa. El usuario debe poder ingresar una temperatura y especificar a qué unidad desea convertirla.

temperature = float(input("Ingresa la temperatura a la cual deseas convertir: "))
type_grade = input("¿Qué grados son, Celsius o Fahrenheit? (c/f): ")

if type_grade == 'c':
    result = temperature*1.8+32
    print(f"De Celsius a Fanhrenheit es: {result}")
else:
    result = (temperature-32)/1.8
    print(f"De Celsius a Fanhrenheit es: {result}")
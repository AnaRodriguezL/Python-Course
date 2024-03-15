# Generador de contraseñas

# Crear un programa que genere contraseñas seguras basándose en criterios especificados por el usuario (longitud, inclusión de caracteres especiales, etc.).

import random
import string

def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_caracteres_especiales):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password

def main():
    print("Generador de contraseñas seguras")

    longitud = int(input("Longitud de la contraseña: "))
    incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_caracteres_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

    password = generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_caracteres_especiales)
    print(f"Tu contraseña segura es: {password}")

if __name__ == "__main__":
    main()

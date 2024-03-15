# Contador de Vocales

# Desarrollar un programa que cuente la cantidad de vocales en una frase proporcionada por el usuario.

contador = 0
vowel = input("Ingresa una palabra: ")

for vowels in vowel:
    if (vowels == 'a') or (vowels == 'e') or (vowels == 'i') or (vowels == 'o') or (vowels == 'u'):
        contador += 1

print(f"Tiene {contador} vocales")
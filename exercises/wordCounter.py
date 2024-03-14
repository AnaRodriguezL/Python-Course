# Contador de palabras

# Dada una cadena de texto, contar cuántas veces aparece cada palabra y presentar los resultados en un diccionario.

texto = "Hola mundo mundo mundo Hola Hola Hola"

# Dividir el texto en palabras
palabras = texto.split()

# Crear un diccionario para almacenar el recuento de palabras
contador_palabras = {}

# Contar la frecuencia de cada palabra
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

# Imprimir el diccionario de recuento de palabras
print("Recuento de palabras:")
print(contador_palabras)
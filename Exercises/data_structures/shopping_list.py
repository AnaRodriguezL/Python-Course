# Lista de la compra

# Crear un programa que permite al usuario ingresar una lista de compras, elemento por elemento, y luego imprima la lista completa al final.

valor = ""
lista_de_compras = []
contador = 0

while valor != "fin":
    valor = input("Por favor ingrese un elemento de la lista de compras: ")
    contador += 1
    if valor != "fin":
        lista_de_compras.append(f"{contador}. {valor}")

print("\n"*20)
for elemento in lista_de_compras:
    print(elemento)
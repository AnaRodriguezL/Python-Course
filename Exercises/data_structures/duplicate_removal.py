# Eliminación de duplicados

# Escribir un programa que tome una lista de números ingresados por el usuario y elimine todos los números duplicados.

list = []

while True:
    number = int(input("Añada un número: "))
    list.append(number)

    decision = input("¿Desea añadir otro número? (s/n): ")

    if decision == 'n':
        print(f"Está es su lista original: {list}")
        for duplicate in list:
            if list.count(duplicate) > 1:
                list.remove(duplicate)
        
        print(f"Está es su lista sin duplicados: {list}")

        break

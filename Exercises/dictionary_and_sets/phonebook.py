# Agenda telefónica

# Crear un programa que permita al usuario añadir, eliminar y buscar números de teléfono en un diccionario.

agenda = {}

while True:
    print("\n1. Añadir número de teléfono")
    print("2. Eliminar número de teléfono")
    print("3. Buscar número de teléfono")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda[nombre] = telefono
        print("Número de teléfono añadido exitosamente.")
    elif opcion == '2':
        nombre = input("Ingrese el nombre para eliminar el número de teléfono: ")
        if nombre in agenda:
            del agenda[nombre]
            print("Número de teléfono eliminado exitosamente.")
        else:
            print("El nombre no está en la agenda.")
    elif opcion == '3':
        nombre = input("Ingrese el nombre para buscar el número de teléfono: ")
        if nombre in agenda:
            print("El número de teléfono de", nombre, "es:", agenda[nombre])
        else:
            print("El nombre no está en la agenda.")
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

# Módulo de Operaciones Matemáticas

# Crear un módulo propio que incluya funciones básicas como suma, resta, multiplicación y división.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

print("Suma:", suma(5, 3))
print("Resta:", resta(10, 4))
print("Multiplicación:", multiplicacion(7, 2))
print("División:", division(8, 2))
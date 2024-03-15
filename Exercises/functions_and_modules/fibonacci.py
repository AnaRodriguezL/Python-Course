# Función de recursividad de Fibonacci

# Implementar una función recursividad que calcule el n-ésimo número de Fibonacci.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo de uso
n = int(input("Ingresa el valor de n para calcular el n-ésimo número de Fibonacci: "))
resultado = fibonacci(n)
print(f"El {n}-ésimo número de Fibonacci es: {resultado}")
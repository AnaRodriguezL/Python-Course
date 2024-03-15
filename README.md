# Python 🐍

## ¿Qué es Python y por qué aprenderlo? 🤔

Python es un lenguaje de programación de alto nivel, interpretado, interactivo y orientado a objetos, creado por el programador neerlandés **Guido Van Rossum a finales de los años 80.** Desde **su lanzamiento en 1991,** Python ha evolucionado significativamente y se ha convertido en uno de los lenguajes de programación más populares del mundo. Se destaca por su sintaxis clara y simple, que facilita su aprendizaje. Además, su capacidad de ser interpretado e interactivo lo hace ideal para una amplia gama de aplicaciones, desde el desarrollo web hasta la ciencia de datos.

*Lo que sigue a continuación son fundamentos que he aprendido en mi curso de Python.*

## Variables 📦

Las variables son contenedores para almacenar datos. Pueden ser pensadas como cajas durante una mudanza: cada caja tiene una etiqueta que identifica su contenido.
```python
# Variables numéricas
numero_entero = 10
numero_decimal = 3.14

# Variables de texto
texto = "¡Hola, mundo!"

# Variables booleanas
verdadero = True
falso = False
```

## Condicionales 🛣️

Las estructuras condicionales permiten que un programa tome decisiones basadas en ciertas condiciones. Son como encrucijadas en un camino: te permiten decidir qué dirección tomar basándote en ciertas condiciones.
```python
# Condicionales para verificar si un número es par o impar
numero = 10
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
```

## Ciclos 🔄

- **Ciclo While:** Se ejecuta un conjunto de instrucciones repetidamente mientras se cumpla una condición específica.
```python
# Ciclo while para imprimir números del 1 al 5
numero = 1
while numero <= 5:
    print(numero)
    numero += 1
```
- **Ciclos For:** Recorren cada elemento en una secuencia de manera ordenada.
```python
# Ciclo for para recorrer una lista e imprimir cada elemento
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
```

## Listas 📋

Las listas son colecciones ordenadas de elementos. Cada elemento en la lista tiene una posición específica y puede ser accedido mediante su índice.
```python
lista = [1, 2, 3, 4, 5]
lista_texto = ["manzana", "banana", "cereza"]
```

## Tuplas 📦🔒

Las tuplas son colecciones ordenadas e inmutables de elementos. A diferencia de las listas, no pueden ser modificadas una vez creadas.
```python
tupla = (1, 2, 3, 4, 5)
tupla_texto = ("rojo", "verde", "azul")
```

## Diccionarios 📚

Los diccionarios son colecciones de pares clave-valor. Cada valor en el diccionario está asociado con una clave única que actúa como su identificador.
```python
# Es similar al formato JSON
diccionario = {
    "nombre": "Juan", 
    "edad": 30, 
    "ciudad": "Madrid"
}
```

## Conjuntos 🌟

Los conjuntos son colecciones desordenadas de elementos únicos. Son útiles cuando se necesita garantizar que cada elemento sea único.
```python
# Variables de conjunto (set)
conjunto = {1, 2, 3, 4, 5}
```

## Funciones 🎯

Las funciones son bloques de código reutilizable que realizan una tarea específica. Ayudan a organizar y modularizar el código, haciéndolo más claro y fácil de mantener.
```python
# Definición de una función para calcular el área de un rectángulo
def calcular_area(base, altura):
    area = base * altura
    return area

# Llamada a la función y almacenamiento del resultado en una variable
base_rectangulo = 5
altura_rectangulo = 3
area_rectangulo = calcular_area(base_rectangulo, altura_rectangulo)
print("El área del rectángulo es:", area_rectangulo)
```

## Módulos 🧰

Los módulos son archivos que contienen código Python. Proporcionan funcionalidades específicas y pueden ser reutilizados en diferentes partes de un programa.
```python
# Creación de un módulo llamado operaciones_matematicas.py
# Este módulo contiene una función para sumar dos números
# Nombre del archivo: operaciones_matematicas.py

def suma(a, b):
    return a + b
```
```python
# Importación del módulo operaciones_matematicas
import operaciones_matematicas

# Uso de la función suma del módulo
resultado_suma = operaciones_matematicas.suma(3, 5)
print("La suma es:", resultado_suma)
```

# Python 🐍

## ¿Qué es Python y por qué aprenderlo? 🤔

Python is a high-level, interpreted, interactive, and object-oriented programming language created by the Dutch programmer Guido Van Rossum in the late 1980s. Since its release in 1991, Python has evolved significantly and has become one of the most popular programming languages in the world. It is known for its clear and simple syntax, which makes it easy to learn. Additionally, its interpretive and interactive nature makes it ideal for a wide range of applications, from web development to data science.

*The following are fundamentals I have learned in my Python course.*

## Variables 📦

Variables are containers for storing data. They can be thought of as boxes during a move: each box has a label identifying its contents.
```python
# Numeric variables
integer_number = 10
decimal_number = 3.14

# Text variables
text = "Hello, world!"

# Boolean variables
true_value = True
false_value = False
```

## Conditionals 🛣️

Conditional structures allow a program to make decisions based on certain conditions. They are like crossroads on a path: they allow you to decide which direction to take based on certain conditions.
```python
# Conditionals to check if a number is even or odd
number = 10
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```

## Loops 🔄

- **While Loop:** Executes a set of statements repeatedly as long as a specific condition is true.
```python
# While loop to print numbers from 1 to 5
number = 1
while number <= 5:
    print(number)
    number += 1
```
- **For Loops:** Iterate over each item in a sequence in an orderly manner.
```python
# For loop to iterate over a list and print each element
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

## Lists 📋

Lists are ordered collections of elements. Each element in the list has a specific position and can be accessed by its index.
```python
list = [1, 2, 3, 4, 5]
text_list = ["apple", "banana", "cherry"]
```

## Tuples 📦🔒

Tuples are ordered and immutable collections of elements. Unlike lists, they cannot be modified once created.
```python
tuple = (1, 2, 3, 4, 5)
text_tuple = ("red", "green", "blue")
```

## Dictionaries 📚

Dictionaries are collections of key-value pairs. Each value in the dictionary is associated with a unique key that acts as its identifier.
```python
# It's similar to JSON format
dictionary = {
    "name": "John", 
    "age": 30, 
    "city": "Madrid"
}
```

## Sets 🌟

Sets are unordered collections of unique elements. They are useful when you need to ensure that each element is unique.
```python
# Set variables
set_variable = {1, 2, 3, 4, 5}
```

## Functions 🎯

Functions are reusable blocks of code that perform a specific task. They help organize and modularize code, making it clearer and easier to maintain.
```python
# Definition of a function to calculate the area of a rectangle
def calculate_area(base, height):
    area = base * height
    return area

# Function call and storing the result in a variable
base_rectangle = 5
height_rectangle = 3
area_rectangle = calculate_area(base_rectangle, height_rectangle)
print("The area of the rectangle is:", area_rectangle)
```

## Modules 🧰

Modules are files that contain Python code. They provide specific functionalities and can be reused in different parts of a program.
```python
# Creation of a module named math_operations.py
# This module contains a function to add two numbers
# File name: math_operations.py

def addition(a, b):
    return a + b
```
```python
# Importing the math_operations module
import math_operations

# Using the addition function from the module
sum_result = math_operations.addition(3, 5)
print("The sum is:", sum_result)
```

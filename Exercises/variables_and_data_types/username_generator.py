# Generador de Nombre de Usuario

# Solicitar al usuario su nombre, apellido y año de nacimiento, y genera un nombre de usuario combinándolo (por ejemplo “AnaSmith1990”).

name = input("Ingrese su nombre: ") # Variable la cual guarda el nombre del usuario al ingresarlo
lastname = input("Ingrese su apellido: ") # Variable la cual guarda el apellido del usuario al ingresarlo
birthdate = input("Ingrese su fecha de nacimiento: ") # Variable la cual guarda la fecha de nacimiento del usuario al ingresarlo

print(f"Bienvenid@ al aplicativo: {name} {lastname} nacido en {birthdate}") #Esta es una forma simplificada para imprimir los datos que requiere ver el usuario
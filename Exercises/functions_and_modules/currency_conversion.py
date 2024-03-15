# Función de Conversión de Divisas

#  Escribir una función que convierta una cantidad de dinero de una moneda a otra utilizando tasas de cambio dadas.

def convertir_moneda(cantidad, tasa_cambio):
    """
    Convierte una cantidad de dinero de una moneda a otra utilizando una tasa de cambio.
    
    Args:
        cantidad (float): La cantidad de dinero a convertir.
        tasa_cambio (float): La tasa de cambio de la moneda original a la moneda objetivo.
        
    Returns:
        float: La cantidad de dinero convertida a la moneda objetivo.
    """
    cantidad_convertida = cantidad * tasa_cambio
    return cantidad_convertida

# Ejemplo de uso
cantidad_original = float(input("Ingrese la cantidad de dinero en la moneda original: "))
tasa_cambio = float(input("Ingrese la tasa de cambio de la moneda original a la moneda objetivo: "))

cantidad_convertida = convertir_moneda(cantidad_original, tasa_cambio)
print("La cantidad convertida es:", cantidad_convertida)
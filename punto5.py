# Definición del decorador
def mostrar_resultado(func):
    """Decorador que imprime el resultado de una función."""
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"Resultado de la operación: {resultado}")
        return resultado
    return wrapper

# Uso del decorador con una función pura
@mostrar_resultado
def sumar(a, b):
    """Función pura que retorna la suma de dos números."""
    return a + b

# Ejemplo de uso
sumar(5, 7)


#Pruebas:
@mostrar_resultado
def multiplicar(x, y):
    return x * y

assert multiplicar(3, 4) == 12
assert sumar(2, 3) == 5

print("Todas las pruebas del decorador pasaron correctamente.")
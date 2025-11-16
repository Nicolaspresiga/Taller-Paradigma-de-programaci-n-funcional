from functools import reduce

def factorial(n: int) -> int:

    
    """Calcula el factorial de un número usando reduce (enfoque funcional).
    Retorna 1 si n es 0 o 1."""
    

    if n < 0:
        raise ValueError("El número debe ser positivo.")
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)



# Pruebas
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(7) == 5040

print("Todas las pruebas del factorial pasaron correctamente.")
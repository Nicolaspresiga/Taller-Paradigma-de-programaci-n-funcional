# Lista original de números
numeros = [-5, -2, 0, 3, 7, -1, 10]

# Función lambda que determina si un número es positivo
positivos = list(filter(lambda x: x > 0, numeros))

print("Números positivos:", positivos)


# Pruebas:

assert list(filter(lambda x: x > 0, [-1, 2, 3, -4])) == [2, 3]
assert list(filter(lambda x: x > 0, [0, 0, 0])) == []
assert list(filter(lambda x: x > 0, [5, 10, 15])) == [5, 10, 15]

print("Todas las pruebas de filtrado de números positivos pasaron correctamente.")
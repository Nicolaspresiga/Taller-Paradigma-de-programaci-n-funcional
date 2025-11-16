
def pares(n, m):
    if n <= 0 or m <= 0 or n >= m:
        raise Exception("No es posible continuar con la operación")

    for numero in range(n, m + 1):
        if numero % 2 == 0:
            yield numero

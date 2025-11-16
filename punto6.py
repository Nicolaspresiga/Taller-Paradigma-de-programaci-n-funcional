def suma(n):
    if n == 1:
        return 1
    else:
        return n + suma(n - 1)

# Programa principal con validación
while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero <= 0:
            print("Por favor ingrese un número mayor que 0.")
        else:
            resultado = suma(numero)
            print(f"La suma de los números de 1 a {numero} es: {resultado}")
            break
    except ValueError:
        print("Error: Debe ingresar un número válido.")



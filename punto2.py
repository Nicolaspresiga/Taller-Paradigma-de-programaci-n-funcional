try:
    base = float(input("Ingrese la base del rectángulo: "))
except ValueError:
    print("Error: Por favor ingrese un número válido para la base.")
try:
    altura = float(input("Ingrese la altura del rectángulo: "))
except ValueError:
    print("Error: Por favor ingrese un número válido para la altura.")

def area(base, altura):
    area = base * altura
    return area

print(f"El área del rectángulo es: {area(base, altura)}")

def validar_email(email):
    if "@" in email:
        return True
    else:
        return False

# Programa principal
correo = input("Ingrese su dirección de correo electrónico: ")

if validar_email(correo):
    print("La dirección es válida ✅")
else:
    print("La dirección no es válida ❌")

def generar_id(nombre_completo: str, dni: str) -> str:
    """
    Genera un identificador único a partir del primer nombre,
    la cantidad de letras del apellido y los primeros 3 dígitos del DNI.
    Ejemplo: 'Alba María Linares', '25834910' → 'Alba7258'
    """
    partes = nombre_completo.strip().split()
    primer_nombre = partes[0].capitalize()
    apellido = partes[-1].capitalize()
    return f"{primer_nombre}{len(apellido)}{dni[:3]}"

def validar_dni(dni: str) -> bool:
    """Verifica que el DNI tenga 7 u 8 dígitos numéricos."""
    return dni.isdigit() and len(dni) in (7, 8)

def obtener_socios():
    """
    Solicita los datos de los socios y genera identificadores.
    Finaliza cuando se ingresa un nombre vacío.
    """
    print("Ingrese los datos de los socios (nombre vacío para terminar):")
    socios = []

    while True:
        nombre = input("Nombre completo: ").strip()
        if not nombre:
            break

        # Validar el DNI
        dni = input("DNI: ").strip()
        while not validar_dni(dni):
            print("El DNI debe tener 7 u 8 dígitos numéricos. Intente nuevamente.")
            dni = input("DNI: ").strip()

        # Generar identificador
        identificador = generar_id(nombre, dni)
        print(f"Identificador generado: {identificador}")

        socios.append((nombre, dni, identificador))

    return socios

# Ejecución principal
if __name__ == "__main__":
    lista_socios = obtener_socios()

    print("\n= LISTA FINAL DE SOCIOS =")
    for nombre, dni, identificador in lista_socios:
        print(f"Socio: {nombre} | DNI: {dni} | ID: {identificador}")
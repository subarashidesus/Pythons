def contar_letras(cadena):
    cuenta = {}
    for letra in cadena:
        cuenta[letra] = cuenta.get(letra, 0) + 1
    return cuenta

# Ejemplo de uso:
cadena = "python"
print(f"Cuenta de letras es '{cadena}' : {contar_letras(cadena)}")

def contar_letras(cadena):
    cuenta = {}
    for letra in cadena:
        cuenta[letra] = cuenta.get(letra, 0) + 1
    return cuenta
# Ejemplo de uso:
cadena = "python"
print(f"Cuenta de letras es  '{cadena}' : {contar_letras(cadena)}")
    
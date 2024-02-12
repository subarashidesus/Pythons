def promedio(lista):
    return sum(lista) / len(lista) if len(lista) > 0 else 0

# Ejemplo de uso:
numeros = [10, 5, 8, 7, 3]
print(f"El promedio de la lista es: {promedio(numeros)}")
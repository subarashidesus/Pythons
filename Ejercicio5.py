def factorial(n):
    return 1 if n == 0 else n * factorial(n -1)

# Ejemplo de uso:
numero = 5
print(f"El factorial de {numero} es: {factorial(numero)}")
def suma_pares(lista):
    return sum(num for num in lista if num % 2 == 0)

# Ejemplo de uso:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"La suma de números pares en la lista es: {suma_pares(numeros)}") 
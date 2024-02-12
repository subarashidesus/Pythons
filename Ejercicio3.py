def es_palindromo(palabra):
    return palabra == palabra[::-1]

# Ejemplo de uso:
palabra = "reconocer"

print(f"{palabra}{'es' if es_palindromo(palabra) else 'no es'} un palíndromo.")
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso:
num = 13
print(f"{num} {'es' if es_primo(num) else 'no es'} un número primo.")

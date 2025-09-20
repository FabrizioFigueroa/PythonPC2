def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def suma_primos_menores_100():
    suma = 0
    for num in range(2, 100):
        if es_primo(num):
            suma += num
    return suma

resultado = suma_primos_menores_100()
print(f"La suma de todos los numeros primos menores que 100 es: {resultado}")

primos = []
for num in range(2, 100):
    if es_primo(num):
        primos.append(num)
print(f"Los numeros primos son: {primos}")
print(f"Total de numeros primos: {len(primos)}")
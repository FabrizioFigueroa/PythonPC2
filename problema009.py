def encontrar_divisores_propios(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(n):
    divisores = encontrar_divisores_propios(n)
    return sum(divisores) == n

def encontrar_numeros_perfectos(limite):
    perfectos = []
    for num in range(1, limite):
        if es_numero_perfecto(num):
            perfectos.append(num)
    return perfectos

numeros_perfectos = encontrar_numeros_perfectos(1000)
print(f"Numeros perfectos menores que 1000: {numeros_perfectos}")

for num in numeros_perfectos:
    divisores = encontrar_divisores_propios(num)
    suma_divisores = sum(divisores)
    print(f"\nNumero perfecto: {num}")
    print(f"Divisores propios: {divisores}")
    print(f"Suma de divisores: {' + '.join(map(str, divisores))} = {suma_divisores}")
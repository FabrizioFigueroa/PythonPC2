def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Ingresa un numero: "))
print(f"{n}! = {factorial(n)}")
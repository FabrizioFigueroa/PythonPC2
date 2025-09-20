def fibonacci_hasta_50():
    fibonacci = []
    a, b = 0, 1
    
    while a <= 50:
        fibonacci.append(a)
        a, b = b, a + b
    
    return fibonacci

serie = fibonacci_hasta_50()
print(f"Serie de Fibonacci entre 0 y 50: {serie}")
print(f"Total de numeros: {len(serie)}")

print("\nPaso a paso:")
a, b = 0, 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b
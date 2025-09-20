numeros = []
pares = 0
impares = 0

while True:
    respuesta = input("¿Desea ingresar un numero?: ").upper()
    if respuesta == "NO":
        break
    
    numero = int(input("Ingrese el numero: "))
    numeros.append(numero)
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

if len(numeros) == 0:
    print("No se ingresaron numeros.")
else:
    print(f"Numeros ingresados: {numeros}")
    print(f"Cantidad de numeros pares: {pares}")
    print(f"Cantidad de números impares: {impares}")
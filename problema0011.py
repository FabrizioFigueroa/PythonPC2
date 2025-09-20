texto = input("Ingrese un texto: ")
for vocal in "aeiouAEIOU":
    texto = texto.replace(vocal, "")
print(texto)
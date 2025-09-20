lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
print("Lista original:", lista_original)

def eliminar_duplicados(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

lista_procesada = eliminar_duplicados(lista_original)
print("Lista procesada:", lista_procesada)
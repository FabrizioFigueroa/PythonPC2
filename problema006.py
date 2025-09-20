n = int(input("Ingrese el numero de alumnos: "))
alumnos = []

for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    
    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }
    alumnos.append(alumno)

print("\nListado completo de alumnos:")
for alumno in alumnos:
    print(alumno)
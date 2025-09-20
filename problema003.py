divisibles_7 = []
multiplos_5 = []

for i in range(1500, 2701):
    if i % 7 == 0:
        divisibles_7.append(i)
    if i % 5 == 0:
        multiplos_5.append(i)

print("Numeros divisibles por 7:", divisibles_7)


print("Numeros multiplos de 5:", multiplos_5)
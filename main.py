matriz = [
    [1, 5, 3],
    [4, 2, 6],
    [9, 8, 7]
]


print("Matriz:")
for fila in matriz:
    print(fila)


num = int(input("Ingrese un número: "))


encontrado = False
es_punto_silla = False


for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] == num:
            encontrado = True

            menor_fila = min(matriz[i])

            columna = [matriz[x][j] for x in range(len(matriz))]
            mayor_columna = max(columna)

            if num == menor_fila and num == mayor_columna:
                es_punto_silla = True


if not encontrado:
    print("El número no está en la matriz.")
else:
    if es_punto_silla:
        print("El número está en la matriz y es un punto de silla.")
    else:
        print("El número está en la matriz pero NO es un punto de silla.")
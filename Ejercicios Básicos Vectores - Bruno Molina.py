def carga_y_recorrido_basico():
    numeros = []
    for x in range(5):
        numero = int(input(f"ingrese el numero{x + 1}:"))
        numeros.append(numero)
        print("los numeros ingresados son:")
    for num in numeros:
        print(num)


def busqueda_y_conteo():
    frutas = ["manzana", "kiwi", "pera", "banana", "uva"]
    frutas_a_buscar = str(input("ingresa el nombre de una fruta: "))
    if frutas_a_buscar in frutas:
        posicion = frutas.index(frutas_a_buscar)
        print(f"la fruta a buscar es {frutas_a_buscar} esta en la posicion {posicion} ")
    else:
        print("la fruta no fue encontrada.")

def suma_y_promedio():
    notas = ["4", "5", "10", "2", "8", "9", "1", "6", "7", "8"]
    suma_total = 0
    for nota in notas:
        suma_total += nota
        promedio = suma_total / len(notas)
        print(f"la suma total es:{suma_total}")
        print(f"promedio:{promedio}")


def Encontrar_el_ValorMáximo_y_Mínimo():
    temperaturas = [20, 100, 90, 50, ]
    max_temp = temperaturas[0]
    min_temp = temperaturas[0]
    for temp in temperaturas:
        if temp > max_temp:
            max_temp = temp
    if temp < min_temp:
        min_temp = temp
    print(f"la temperatura maxima es:{max_temp}")
    print(f"la temperatura minima es:{min_temp}")


def Ordenamiento():
    numeros = [21, 3, 5, 13, 30, 40, ]
    for x in range(len(numeros)):
        for i in range(i + 1, len(numeros)):
            if numeros[i] < numeros[i]:
                numeros[i], numeros[i] = numeros[x], numeros[i]
    print("lista ordenada de forma ascendente:")


def Pares_e_Impares():
    numeros = [3, 6, 7, 8, 10, 34, 5, 6, 78, 31, ]
    pares = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"cantidad de numeros pares:{pares}")
    print(f"cantidad de numeros impares:{impares}")
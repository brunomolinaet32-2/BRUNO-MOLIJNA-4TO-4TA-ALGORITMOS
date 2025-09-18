def busqueda_secuencial():
   mi_arreglo = [15, 2, 8, 19, 4, 12, 7]
   valor_a_buscar = 19
   for i in range(len(mi_arreglo)):
       if mi_arreglo[i] == valor_a_buscar:
         return i  # Se encontró el valor, se retorna su índice
   return -1  # No se encontró el valor




def busqueda_binaria():
   arreglo = [2, 4, 7, 8, 12, 15, 19]
   valor = 12
   izquierda = 0
   derecha = len(arreglo) - 1


   while izquierda <= derecha:
       medio = (izquierda + derecha) // 2  # Se calcula el índice central
       if arreglo[medio] == valor:
           return medio  # Se encontró el valor
       elif arreglo[medio] < valor:
           izquierda = medio + 1  # El valor está en la mitad derecha
       else:
           derecha = medio - 1  # El valor está en la mitad izquierda
   return -1  # No se encontró el valor



def ordenamiento_insercion():
   lista = [64, 34, 25, 12, 22, 11, 90]
   # Se recorre la lista desde el segundo elemento
   for i in range(1, len(lista)):
       key = lista[i]  # Elemento a insertar
       j = i - 1


       # Se mueven los elementos de la sublista ordenada que son mayores que key
       # una posición a la derecha
       while j >= 0 and key < lista[j]:
           lista[j + 1] = lista[j]
           j -= 1


       # Se inserta key en su posición correcta
       lista[j + 1] = key
   return lista



def ordenamiento_burbuja():
   lista = [64, 34, 25, 12, 22, 11, 90]
   n = len(lista)
   # n-1 pasadas
   for i in range(n - 1):
       # La bandera para optimización
       Hay_Cambio = False
       # n-i-1 comparaciones en cada pasada
       for j in range(0, n - i - 1):
           # Se comparan elementos adyacentes
           if lista[j] > lista[j + 1]:
               # Si están en el orden incorrecto, se intercambian
               lista[j], lista[j + 1] = lista[j + 1], lista[j]
               Hay_Cambio = True
       # Si no hubo intercambios en la pasada, la lista está ordenada
       if not Hay_Cambio:
           break
   return lista

def ordenamiento_seleccion():
   lista = [64, 34, 25, 12, 22, 11, 90]
   n = len(lista)
   # Se recorre la lista hasta el penúltimo elemento
   for i in range(n):
       # Se asume que el elemento actual es el mínimo
       minimo = i
       # Se busca el elemento mínimo en el resto de la lista
       for j in range(i + 1, n):
           if lista[j] < lista[minimo]:
               minimo = j
       # Se intercambia el elemento mínimo encontrado con el primer elemento del segmento no ordenado
       lista[i], lista[minimo] = lista[minimo], lista[i]
   return lista



def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1 - Crear lista y agregar elementos")
    print("2 - Buscar en la lista")
    print("3 - Ordenar la lista")
    print("4 - Salir")


def main():
    lista = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            lista = []
            print("Ingresa los elementos de la lista (separados por espacio):")
            elementos = input().split()

            try:
                lista = [int(e) for e in elementos]
            except ValueError:
                lista = elementos
            print("Lista creada:", lista)

        elif opcion == "2":
            if not lista:
                print("La lista está vacía. Crea la lista primero.")
                continue
            print("Método de búsqueda:")
            print("a) Secuencial")
            print("b) Binaria (requiere lista ordenada)")
            metodo = input("Elige a/b: ").lower()
            dato = input("Elemento a buscar: ")
            try:
                dato = int(dato)
            except ValueError:
                pass
            if metodo == "a":
                pos = busqueda_secuencial(lista, dato)
            else:
                pos = busqueda_binaria(sorted(lista), dato)
            if pos != -1:
                print(f"Elemento encontrado en la posición {pos}")
            else:
                print("Elemento no encontrado")

        elif opcion == "3":
            if not lista:
                print("La lista está vacía. Crea la lista primero.")
                continue
            print("Método de ordenamiento:")
            print("a) Inserción")
            print("b) Burbuja")
            print("c) Selección")
            metodo = input("Elige a/b/c: ").lower()
            if metodo == "a":
                ordenamiento_insercion(lista)
            elif metodo == "b":
                ordenamiento_burbuja(lista)
            else:
                ordenamiento_seleccion(lista)
            print("Lista ordenada:", lista)

        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()


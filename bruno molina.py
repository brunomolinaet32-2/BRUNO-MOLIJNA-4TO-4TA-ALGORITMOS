def cifrado_cesar():
   mensaje = input("Ingresar un mensaje: ")
   clave = int(input("Ingresar clave de cifrado (número): "))
   alfabeto = "abcdefghijklmnñopqrstuvwxyz"
   mensaje_cifrado = ""
   mensaje = mensaje.lower()
   for letra in mensaje:
       if letra in alfabeto:
           posicion_actual = 0
           for i in range(len(alfabeto)):
               if alfabeto[i] == letra:
                   posicion_actual = i
           nueva_posicion = posicion_actual + clave


           # si se pasa del final del abecedario vuelve al inicio
           while nueva_posicion >= len(alfabeto):
               nueva_posicion = nueva_posicion - len(alfabeto)


           # agrego la nueva letra
           mensaje_cifrado = mensaje_cifrado + alfabeto[nueva_posicion]
       else:
           # si no es letra, la dejo igual (espacio, número, coma, etc.)
           mensaje_cifrado = mensaje_cifrado + letra


   print("Mensaje cifrado:", mensaje_cifrado)
cifrado_cesar()


def ejercicio1():
   frutas = ["manzana", "banana", "cereza"]


   print("Lista completa:", frutas)
   print("La segunda fruta es:", frutas[1])


def ejerciccio2():
   animales = ["perro", "gato", "elefante"]
   animales.append("jirafa")
   animales.remove("gato")


   print("Lista de animales:", animales)


def ejercicio3():
   lista1 = [5, 1, 8]
   lista2 = [3, 9, 2]


   lista_completa = lista1 + lista2
   print("Lista completa:", lista_completa)


   total = 0
   for numero in lista_completa:
       total = total + numero


   print("Total:", total)


def ejercicio4():
   lista1 = [5, 1, 8]
   lista2 = [3, 9, 2]


   lista_final = lista1 + lista2


   print("La lista final es:", lista_final)


def ejercicio5():
   import random


   nombres = ["Pepe", "Juana", "Santiago", "Ignacio", "Federico", "Gabriel", "Sofia"]
   notas = [1,2,3,4,5,6,7,8,9,10]


   Alumno = []


   Alumno.append(random.choice(nombres))
   Alumno.append(random.choice(notas))


   print("Alumno generado automáticamente:", Alumno)


def ejercicio6():
   Alumno1 = [9, 7, 8]
   Alumno2 = [6, 5, 4]
   Alumno3 = [10, 9, 8]


   # sumamos manualmente
   total1 = 0
   for nota in Alumno1:
       total1 = total1 + nota
   promedio1 = total1 / 3


   total2 = 0
   for nota in Alumno2:
       total2 = total2 + nota
   promedio2 = total2 / 3


   total3 = 0
   for nota in Alumno3:
       total3 = total3 + nota
   promedio3 = total3 / 3


   PromedioCurso = (promedio1 + promedio2 + promedio3) / 3


   print("Promedio del curso:", PromedioCurso)




def ejrcicio7():
   promedios = []
#profe aca podes agregar las notas de los promedios y dependiendo de eso te va tirar si es bueno o malo.
   promedios.append(7)
   promedios.append(8)
   promedios.append(6)


   total_prom = 0
   for prom in promedios:
       total_prom = total_prom + prom


   promedio_escuela = total_prom / 3


   print("Promedio general:", promedio_escuela)


   if promedio_escuela >= 6:
       print("La escuela tiene buenos promedios.")
   else:
       print("La escuela tiene malos promedios.")

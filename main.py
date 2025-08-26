def ejercicio1():
 matriz=[[1,2,3],
        [4,5,6,],
        [7,8,9]]
 for x in range(len(matriz)):
  print(matriz[x])
ejercicio1()



def ejercicios2():
 suma=0
 matriz=[[10,20,30],
    [40,50,60],
    [70,80,90]]
 for fila in matriz:
  for num in fila:
      suma += num
 for x in range(len(matriz)):
  print(f"la total de la suma es:{suma}")
ejercicios2()


def ejercicio3():
 matriz=[[10,20,30,40],
        [50,60,70,80],
        [90,100,110,120],
        [130,140,150,160]]
 for fila in matriz:
    print(fila)
 fila=(int(input("ingrese el indice para la fila 0-3:")))
 columna=int(input("ingrese el indice para la columna 0-3:"))
 print(f"el numero en esa posicion es",matriz[columna][fila])
ejercicio3()

def ejercicio4():
 matriz = [[10, 20, 30, 40],
         [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160]]
 mayor=max(max(fila)for fila in matriz)
 print(f"el numerio mas grande de la matriz es:",mayor)
ejercicio4()
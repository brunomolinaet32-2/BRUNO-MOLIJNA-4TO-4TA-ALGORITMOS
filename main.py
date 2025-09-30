def calculadora1():
    precio=float(input("ingrese su precio."))
    if precio>=100:
         print("se aplica un descuento del 15%.")
    elif precio >=50 or 99.99:
     print("se aplica un descuento de 10%.")
    elif precio<50:
        print("no hay descuento.")
def adivina_el_numero_secreto():
    numero_secreto = 7
    adivinado = False
    while not adivinado:
        numero = int(input("Adivina el número secreto: "))
        if numero == numero_secreto:
            print("Felicidades, adivinaste el número secreto")
            adivinado = True
        elif numero < numero_secreto:
            print("El número ingresado es menor")
        else:
            print("El número ingresado es mayor")
adivina_el_numero_secreto()

def contador_de_vocales():
   vocales = "AEIOUaeiuo"
   texto=("chenchon")
   contador_vocales=0
   for caracter in (texto):
        if caracter.lower() in vocales :
             contador_vocales += 1
   return contador_vocales
contador_de_vocales()
def tabla_de_multiplicar():
   num_entero = 0
   opc = int(input("Ingrese un Número:"))
   for x in range(1 , 10+1):
        num_entero = opc * x
   print(num_entero)
   return num_entero
tabla_de_multiplicar()
def ejercicio5():
 suma = 0
 while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
     break
    if numero % 2 == 0:
     suma += numero
     print("La suma de los números pares es:", suma)

ejercicio5()
def menu():
   quiere_seguir = True
   while quiere_seguir == True:
       opc = int(input("""
       --------------------------------------------
       1.calculadora
       2. numero secreto
       3.contador de vocales
       4.tabla de multiplicar
       5.suma de numeros pares
      
       --------------------------------------------
       Seleccione un número: """))
       if opc == 0:
           print("Saliendo del programa...")
           quiere_seguir = False
       elif opc == 1:
           calculadora1()
       elif opc == 2:
           adivina_el_numero_secreto()
       elif opc == 3:
           contador_de_vocales()
       elif opc == 4:
        print("el programa se cierra.")



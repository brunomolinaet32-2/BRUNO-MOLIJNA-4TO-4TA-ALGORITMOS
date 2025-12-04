def ejercicio6():
    n=int(input("ingrese un numero entero: "))
    if n>0:
          print("el numero es positivo")

def ejercicio7():
   edad=int(input("ingrese su edad: "))
   if edad>=18:
       print("¡Bienvenido a la fiesta!")
   else:
       print("Lo siento, eres muy joven")


def ejercicio8():
   clave=(input("ingrese su contraseña: "))
   if clave=="python123":
       print("¡Contraseña correcta! Acceso concedido.")
   else:
       print("¡Contraseña incorrecta, Autodestrucción en 5 minutos!")


def ejercicio9():
   numero=int(input("ingrese un numero entero: "))
   if numero % 2 :
       print("el numero  es  impar.")
   else:
       print("el numero es par.")
def ejercicio10():
   edad=int(input("ingrese su edad."))
   palomitas=int(input("compraste palomitas?"))
   if edad>=65 and palomitas == "si":
    print("¡Felicidades! Tienes entrada gratuita al cine.")
   else:
    print("Compra la entrada o raja de acá.")

def ejercicio11():
    contador=5
    while contador>0:
        print(contador)
        contador-=1
        print("Listo para despegar")
        print("Despegue")

def ejercicio12():
    secreto=7
    num=int(input("adivina el numero:"))
    while num !=secreto:
        print("incorrecto,intenta otra vez")
        num=int(input("adivina el nunero:"))
        print("¡Felicidades! Adivinaste el número.")

def ejercicio13():
    suma=0
    numeros=int(input("ingrese un numero  para finalizar:"))
    while numeros!=0:
     suma+=numeros
     numeros = int(input("ingrese otro  numero  para finalizar:"))
    print("la suma total es:", suma)


def ejercicio1():
 contador=0
 for numero in range (1,11):
  print(numero)
def ejercicio2():
   contador=0
   for x in range (1,6):
       print("hola mundo")
def ejercicio3():
  for x  in range(2,2,21):
      print(x)

def ejercicio4():
  for x in range(7,71,7):
      print(x)

def ejercicio5():
    suma=0
    for x in range(1,6):
        suma+=x
        print("la suma es ",suma)


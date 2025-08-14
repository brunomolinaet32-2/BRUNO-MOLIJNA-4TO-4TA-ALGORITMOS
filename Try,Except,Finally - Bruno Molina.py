def dividir_numeros():
    try:
        num1 = int(input("ingrese el primer numero:"))
        num2 = int(input("ingrese el segundo numero:"))
        resultado = num1 / num2
        print(f"el resultado de la divison es:{resultado}")
    except ZeroDivisionError:
        print("¡No se puede dividir por cero!")
    except ValueError:
        print("ingrese un valor no numerico:")
    finally:
        print("fin del intento de division")
    dividir_numeros()


def pedir_edad():
    while True:
        try:
            edad = int(input("ingrese tu edad:"))
            print(f"tu edad es[{edad}")
            break
        except ValueError:
            print("porfavir ingresa un valor numerico entero")


pedir_edad()


def nombres():
    nombres = ["ana", "pedro", "sofia"]
    try:
        indice = input("ingresa un numero indice:")
        print(f"nombre: {nombres[indice]}")
    except IndexError:
        print("error el indice esta fuera del rango de la lista")
    except ValueError:
        print("erro ,ingresaste un valor que no es el numero:")


nombres()


def suma_de_numeros():
    try:
        num1 = ("ingrese un numero entero:")
        num2 = ("ingrese otro numero entero:")
        resultado = num1 + num2
        print(resultado)
    except  ValueError:
        print("uno de los dos numeros ingresados no es valido")


suma_de_numeros()


def division_de_numeros():
    try:
        a = int(input())
        b = int(input())
        resultado = a / b
        print(f"el resultado de la division es{resultado}")
    except ZeroDivisionError:
        print("erorr: no se puede dividir por cero")
    except ValueError:
        print("ingresaste un valor invalido")
    finally:
        print("fin del rpograma de calculo")
    division_de_numeros()

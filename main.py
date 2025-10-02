def ejercicio1():
    informacion_personal = {
        "nombre": "bruno",
        "edad": 17,
        "ciudad": "new york",
        "profesion": "estudiante"
    }
    print(informacion_personal)

def ejercicio2():
    informacion_personal = {
        "nombre": "bruno",
        "edad": 17,
        "ciudad": "madrir",
        "profesion": "programador"
    }

    informacion_personal["ciudad"] = "buenos aires"
    informacion_personal["profesion"] = "estudiante"
    informacion_personal["telefono"] = 1173613793
    informacion_personal["mail"]= "bruno.molinaet32@gmail.com"

    print(informacion_personal)

def ejercicio3():
    calificaciones = {
        "matematicas": 8,
        "lengua": 7,
        "Ciencias": 5
    }
    print(calificaciones["matematicas"])

def ejercicio4():
    calificaciones = {
        "matematicas": 8,
        "lengua": 7,
        "Ciencias": 5
    }

    promedio= sum(calificaciones.values()) / len(calificaciones)



    print(promedio)

def ejercicio5():
    paises_capitales = {
        "argentina":"buenos aires",
        "españa":"madrid",
        "mexico":"ciudad de mexico"
    }


    while True:
        elegir = int(input("""ingresá un pais en el que quieras saber la capital
                  1-argentina
                  2-españa
                  3-mexico
                  :"""))

        if elegir == 1:
            print(paises_capitales["argentina"])


        elif elegir == 2:
            print(paises_capitales["españa"])

        elif elegir == 3:
            print(paises_capitales["mexico"])

        else:
            print("elegi un pais valido")


def ejercicio6():

    precios = {
        "pan": 1000,
        "leche": 3000,
        "arroz": 2500,
        "huevos": 5000
    }


    def costo_total(producto, cantidad):
        if producto in precios:
            return precios[producto] * cantidad
        else:
            return "producto no disponible"


    print(costo_total("pan", 3))
    print(costo_total("leche", 2))
    print(costo_total("carne", 1))

def ejercicio7():
    informacion_personal = {
        "nombre": "bruno",
        "edad": 17,
        "ciudad": "new york",
        "profesion": "estudiante",
        "telefono": 1173613793
    }

    del informacion_personal["telefono"]

    print(informacion_personal)

def ejercicio8():
    dic = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    print(dic.get("a") )
    print(dic.get("z"))

def ejercicio9():
    dic = {
        "a": 1,
        "b": 2,
        "c": 3
    }

    dic2 = {
        "d": 4,
        "f": 5,
        "g": 3
    }

    dic3 = dic|dic2

    print(dic3)




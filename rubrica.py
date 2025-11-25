import mysql.connector
from mysql.connector import errorcode
import datetime

cursor = None
cnx = None

# ==============================
# CONEXIÓN A LA BASE DE DATOS
# ==============================
def conectarBase():
    global cnx, cursor
    try:
        cnx = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="rubricas_db"
        )
        cursor = cnx.cursor(dictionary=True)
        print("Conexión establecida")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o contraseña incorrectos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)

conectarBase()


# ==============================
# CONSULTA SELECT GENÉRICA
# ==============================
def consultaSelect(tabla):
    Consulta = f"SELECT * FROM {tabla};"
    cursor.execute(Consulta)
    return cursor.fetchall()


# ==============================
# AGREGAR NUEVA RÚBRICA
# ==============================
def agregarRubrica():
    nombre = input("Ingrese el nombre de la nueva rúbrica: ")

    sql = "INSERT INTO rubricas (nombre) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    cnx.commit()

    rubrica_id = cursor.lastrowid
    print(f"✔ Rúbrica creada con ID {rubrica_id}")

    agregarCriterios(rubrica_id)


# ==============================
# AGREGAR CRITERIOS A UNA RÚBRICA
# ==============================
def agregarCriterios(rubrica_id):
    print("\nIngrese criterios para esta rúbrica")
    print("Escriba 'fin' para dejar de agregar\n")

    while True:
        nombre = input("Nombre del criterio: ").strip()

        if nombre.lower() == "fin":
            print("✔ Criterios cargados correctamente")
            break

        puntaje = int(input("Puntaje máximo del criterio: "))

        sql = """
            INSERT INTO criterios (rubrica_id, nombre, puntaje_max)
            VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (rubrica_id, nombre, puntaje))
        cnx.commit()

        print("Criterio agregado ✓\n")


# ==============================
# MOSTRAR TODAS LAS RÚBRICAS
# ==============================
def mostrarRubricas():
    rubricas = consultaSelect("rubricas")

    if not rubricas:
        print("No hay rúbricas registradas.")
        return None

    print("\n===== LISTA DE RÚBRICAS =====")
    for rub in rubricas:
        print(f"{rub['id']}) {rub['nombre']}")

    return rubricas


# ==============================
# MOSTRAR RÚBRICA COMPLETA (con criterios)
# ==============================
def mostrarRubricaCompleta():
    rubricas = mostrarRubricas()
    if not rubricas:
        return

    elegido = int(input("\nIngrese el ID de la rúbrica que desea ver: "))

    # Buscar la rubrica seleccionada
    cursor.execute("SELECT * FROM rubricas WHERE id=%s", (elegido,))
    rubrica = cursor.fetchone()

    if not rubrica:
        print("ID inválido")
        return

    print(f"\n=== {rubrica['nombre']} ===")

    # Mostrar criterios asociados
    cursor.execute("SELECT * FROM criterios WHERE rubrica_id=%s", (elegido,))
    criterios = cursor.fetchall()

    if not criterios:
        print("Esta rúbrica no tiene criterios")
        return

    for c in criterios:
        print(f"- {c['nombre']} (máx {c['puntaje_max']})")


# ==============================
# MENÚ PRINCIPAL
# ==============================
def menu():
    while True:
        opcion = int(input("""
===========================
     MENÚ DE RÚBRICAS
===========================
1) Crear nueva rúbrica
2) Mostrar todas las rúbricas
3) Mostrar rúbrica completa
4) Salir
Ingrese opción: """))

        if opcion == 1:
            agregarRubrica()

        elif opcion == 2:
            mostrarRubricas()

        elif opcion == 3:
            mostrarRubricaCompleta()

        elif opcion == 4:
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


menu()
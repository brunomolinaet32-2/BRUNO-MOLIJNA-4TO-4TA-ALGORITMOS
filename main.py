
import mysql.connector

from mysql.connector import errorcode

#Hola chicos hoy no van a tener texto afuera, vamos a trabajar aca directamente,
#probablemente yo este en unas charlas toda la mañana asi que necesito que presten atencion para que puedan ir avanzando
#este codigo que arme es una conexion a base de datos simple, para una base de datos que les creo sofi
#les voy a dejar el codigo abajo para crear la tabla para que puedan practicar
#les recomiendo que practiquen con este codigo primero y luego van a hacer unos ejercicios con esto
#primero lo primero no se olviden de abrir el Xammp y abrir la base de datos en el workbench sino no va a funcionar
# y tambien copien el codigo para crear las tablas que les dio sofi
# recuerden sofi no les creo la base de datos como tal sino la ejecucion para que tengan todas las tablas armadas

#---------------------------------------------------------------------------------------------------------------------#

#empezemos, si me dieron bola en general tiene una idea de lo que son las variables globales y el pasaje de datos
#para este ejemplo y para la simplicidad general del codigo vamos a crear dos variables globales, una llamada cursor
# y una llamada conexion y les vamos a poner valores nulos


cursor = None
cnx = None

#vamos a separar de manera prolija nuestro codigo en diferentes funciones, siendo la primera la conexion con la base de
#datos

def ConectarBase():
    # lo primeros que hacemos es poner global a nuestras variables, esto significa que no solo va a usar las variables
    #globales sino que cuando estas variables las cambie esta porcion del codigo tambien van a guardarse globalmente
    global cnx, cursor

    #una vez hecho esto abrimos una estructura try except, ya que la conexion puede fallar por muchos factores y no
    # queremos que nuestro codigo pare
    try:
        #vamos a instanciar que nuestra variable va a ser igual a lo que devuelva el metodo connect
        #este puede recibir mucho valores, nosotros tenemos que decirle que valor es y el valor como tal
        #vamos a estructurarlo de la siguiente manera, usuario, contraseña, host y nombre de la base
        cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="holi")
        # cursor es la variable con la que nos vamos a referir a las lineas de consulta que les vamos a mandar
        cursor = cnx.cursor(dictionary=True)
        print('Conexión establecida')

    #luego hacemos un except con los errores
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuario o contraseña incorrectos!')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe!')
        else:
            print(err)
#una vez hecho esa parte del codigo, vamos a tener esas 2 variables prontas para usar
#lo siguiente es hacer las consultas que es la parte mas facil
#solamente instanciamos un string con la consulta adentro
#y luego ponemos cursor.execute(consulta)
# si queremos guardar el valor le decimos que queremos metodo fetchall() del cursor
#esto nos va a devolver todas las filas de la consulta que se ejecuto
#esto  NO CAMBIA NADA DE LA BASE DE DATOS, para que lo haga tenemos que poner conexion.commit
#pero para hacer un select no necesitamos cambiar nada de la base de datos
def ConsultaSelect():
    Consulta = "SELECT * FROM clientes;"
    cursor.execute(Consulta)
    return cursor.fetchall()

#para insertar es la misma tarea, pero vamos a cambiar un poco como hacemos las consultas que comunmente hacemos
#hay muchas formas en las que pueden vulnerar nuestras base de datos, una de ellas es añadiendo codigo a nuestras
#consultas, para evitar esto, jamas tenemos que escribir nuestras consultas enteras
#tenemos que hacer consultas parametrizadas, lo que significa que cada valor va a ser un parametro, que luego nosotros
#enviamos cuando ejecutamos el metodo execute
#traduciendolo a python lo que tenemos que hacer es poner %s en cada valor de la consulta en vez de poner el valor
#luego cuando ejecutamos cursor.execute le pasamos como parametro no solo la consulta si no tambien el valor de los
#datos en orden
#en este caso los datos se los pasamos cuando ejecutamos la funcion y deberian de estructurarlo asi siempre

def ConsultaInsertar(nombre,dni,correo,saldo):
    sql = "INSERT INTO clientes (nombre, dni, correo, saldo)VALUES( %s, %s, %s, %s)"
    cursor.execute(sql,(nombre,dni,correo,saldo))
    cnx.commit()
    return cursor.lastrowid

#una vez hechas ambas funciones vamos a ejecutar la conexion de la base de datos y luego vamos a ejecutar la funcion
#insertar para que inserte lo que queremos a la tabla
#luego vamos a imprimir lo que devuelve ConsultaSelect para ver si se ejecuto de manera correcta

ConectarBase()
ConsultaInsertar("pesdsaasd",94975861,"roberto@gmail.com",500.00)
print(ConsultaSelect())
#por ulitmo vamos a cerrar la base de datos, lo cual es extremadamente importante y no nos tenemos que olvidar
if cnx.is_connected():
    cnx.close()
    print("La conexión a la base de datos ha sido cerrada.")
#recuerden que lo que devuelve la base de datos es un diccionario o una lista de diccionarios, asi que a partir
#de ahi trabajan como normalmente trabajarian con la base de datos
#les voy a dejar unos ejercicios que van a usar esta base de datos, intenten estructuralos en diferente funciones
#dentro de este mismo codigo

import sqlite3
import json
import os  # Para verificar si el archivo de la base de datos existe

NOMBRE_DB = 'mi_base_datos.db'


# --- Funciones Auxiliares ---

def conectar_db(db_name=NOMBRE_DB):
    """Establece la conexión a la base de datos."""
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def inicializar_db():
    """Crea la base de datos y la tabla 'productos' si no existen, e inserta datos de ejemplo."""
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        try:
            # Crear tabla
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL
                )
            """)

            # Insertar datos de ejemplo solo si la tabla está vacía
            cursor.execute("SELECT COUNT(*) FROM productos")
            if cursor.fetchone()[0] == 0:
                print("Insertando datos de ejemplo...")
                datos_ejemplo = [
                    ('Laptop', 1200.00),
                    ('Ratón', 25.50),
                    ('Teclado', 75.99),
                    ('Monitor', 350.00)
                ]
                cursor.executemany("INSERT INTO productos (nombre, precio) VALUES (?, ?)", datos_ejemplo)

            conn.commit()
            print(f"Base de datos '{NOMBRE_DB}' e tabla 'productos' listas.")
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")
        finally:
            conn.close()


# --- Funciones de Ejercicio (CRUD y Utilidades) ---

def ejercicio_1_imprimir_tabla():
    """Ejercicio 1: Imprime una tabla seleccionada por el usuario, una fila debajo de la otra."""
    tabla = input("Ingrese el nombre de la tabla a imprimir (ej. productos): ").strip()
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        try:
            # Consulta para obtener las filas y los nombres de las columnas
            cursor.execute(f"SELECT * FROM {tabla}")
            filas = cursor.fetchall()

            if not filas:
                print(f"La tabla '{tabla}' está vacía o no existe.")
                return

            # Obtener los nombres de las columnas
            nombres_columnas = [description[0] for description in cursor.description]

            print(f"\n--- Contenido de la tabla '{tabla}' ---")

            # Imprimir encabezado
            print("| " + " | ".join(nombres_columnas) + " |")
            print("-" * (sum(len(c) for c in nombres_columnas) + len(nombres_columnas) * 3 + 1))

            # Imprimir filas
            for fila in filas:
                valores = [str(col) for col in fila]
                print("| " + " | ".join(valores) + " |")

        except sqlite3.OperationalError as e:
            print(f"Error: {e}. Asegúrese de que la tabla '{tabla}' exista.")
        finally:
            conn.close()


def ejercicio_2_crear_json():
    """Ejercicio 2: Crea un archivo JSON con el contenido de una tabla completa."""
    tabla = input("Ingrese el nombre de la tabla para crear el archivo JSON (ej. productos): ").strip()
    nombre_archivo = f"{tabla}.json"
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM {tabla}")
            filas = cursor.fetchall()

            if not filas:
                print(f"La tabla '{tabla}' está vacía o no existe.")
                return

            # Obtener los nombres de las columnas
            nombres_columnas = [description[0] for description in cursor.description]

            # Convertir las filas (tuplas) a una lista de diccionarios
            datos_json = []
            for fila in filas:
                registro = dict(zip(nombres_columnas, fila))
                datos_json.append(registro)

            # Escribir a archivo JSON
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                json.dump(datos_json, f, indent=4)

            print(f"Archivo '{nombre_archivo}' creado exitosamente con {len(datos_json)} registros.")

        except sqlite3.OperationalError as e:
            print(f"Error: {e}. Asegúrese de que la tabla '{tabla}' exista.")
        except Exception as e:
            print(f"Ocurrió un error al crear el archivo JSON: {e}")
        finally:
            conn.close()


def ejercicio_3_imprimir_consulta_select():
    """Ejercicio 3: Imprime el resultado de una consulta SELECT dictada por el usuario (solo los valores a seleccionar)."""
    print("\n--- Consulta SELECT Personalizada ---")
    columnas = input("Ingrese las columnas a seleccionar (ej. nombre, precio): ").strip()
    tabla = input("Ingrese la tabla (ej. productos): ").strip()
    condicion = input("Ingrese la condición WHERE (ej. precio > 100) o déjelo vacío: ").strip()

    sql = f"SELECT {columnas} FROM {tabla}"
    if condicion:
        sql += f" WHERE {condicion}"

    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()

            if not resultados:
                print("No se encontraron resultados para la consulta.")
                return

            # Imprimir los resultados (solo los valores, como se pidió)
            print("\n--- Resultado de la Consulta ---")
            for fila in resultados:
                print(tuple(fila))  # Imprime la tupla de valores de cada fila

        except sqlite3.OperationalError as e:
            print(f"Error de consulta SQL: {e}")
            print("Verifique que las columnas, la tabla y la sintaxis sean correctas.")
        finally:
            conn.close()


def ejercicio_4_update():
    """Ejercicio 4: Cambia un valor de un elemento ya existente (UPDATE)."""
    print("\n--- Modificar Registro (UPDATE) ---")
    tabla = input("Ingrese el nombre de la tabla a modificar (ej. productos): ").strip()
    campo_modificar = input("Ingrese el nombre del campo a modificar (ej. precio): ").strip()
    nuevo_valor = input(f"Ingrese el nuevo valor para '{campo_modificar}': ").strip()
    campo_condicion = input("Ingrese el nombre del campo de la condición (ej. id): ").strip()
    valor_condicion = input(f"Ingrese el valor para la condición '{campo_condicion}' (ej. 1): ").strip()

    # Usar '?' como marcador de posición para evitar inyección SQL
    sql = f"UPDATE {tabla} SET {campo_modificar} = ? WHERE {campo_condicion} = ?"

    # Intenta convertir el valor de condición a entero si el campo es 'id', por ejemplo.
    try:
        if campo_condicion.lower() == 'id':
            valor_condicion = int(valor_condicion)
    except ValueError:
        pass  # Se mantiene como string si falla la conversión

    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        try:
            # Manejar si el nuevo valor necesita comillas o no (simplificación)
            # En SQLite, no necesitamos manejar esto si usamos el marcador '?'
            cursor.execute(sql, (nuevo_valor, valor_condicion))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"\nÉxito: Se actualizó {cursor.rowcount} registro(s) en '{tabla}'.")
            else:
                print("\nAdvertencia: No se encontró ningún registro para actualizar.")

        except sqlite3.OperationalError as e:
            print(f"Error de actualización SQL: {e}")
            print("Verifique que la tabla, los campos y la sintaxis sean correctos.")
        finally:
            conn.close()


def ejercicio_5_insertar_datos():
    """Ejercicio 5: Inserta datos puestos por el usuario en una tabla elegida (INSERT)."""
    print("\n--- Insertar Nuevo Registro (INSERT) ---")
    tabla = input("Ingrese el nombre de la tabla para insertar (ej. productos): ").strip()

    # NOTA: Esta implementación asume la tabla 'productos' con campos 'nombre' y 'precio'.
    # Para hacerlo genérico, se necesitaría obtener la estructura de la tabla primero.

    if tabla.lower() == 'productos':
        nombre = input("Ingrese el nombre del producto: ").strip()
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: ").strip())
                break
            except ValueError:
                print("El precio debe ser un número. Intente de nuevo.")

        sql = f"INSERT INTO {tabla} (nombre, precio) VALUES (?, ?)"
        parametros = (nombre, precio)
    else:
        # Aquí iría la lógica para obtener dinámicamente los campos de otras tablas.
        print("Esta función solo soporta la tabla 'productos' en este ejemplo simple.")
        return

    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(sql, parametros)
            conn.commit()
            print(f"\nÉxito: Se insertó un nuevo registro en la tabla '{tabla}' con ID: {cursor.lastrowid}")

        except sqlite3.OperationalError as e:
            print(f"Error de inserción SQL: {e}")
            print("Verifique que la tabla y los campos sean correctos.")
        finally:
            conn.close()


# --- Ejercicio 6: Menú Principal ---

def ejercicio_6_menu_principal():
    """Ejercicio 6: Función que une todo en un menú interactivo."""
    opciones = {
        '1': ("Imprimir Tabla Completa", ejercicio_1_imprimir_tabla),
        '2': ("Crear Archivo JSON de Tabla", ejercicio_2_crear_json),
        '3': ("Imprimir Resultado de Consulta SELECT", ejercicio_3_imprimir_consulta_select),
        '4': ("Modificar un Registro (UPDATE)", ejercicio_4_update),
        '5': ("Insertar un Nuevo Registro (INSERT)", ejercicio_5_insertar_datos),
    }

    while True:
        print("\n" + "=" * 40)
        print(" " * 10 + "📋 MENÚ DE BASE DE DATOS SQLITE")
        print("=" * 40)

        for clave, (descripcion, _) in opciones.items():
            print(f"{clave}. {descripcion}")

        print("0. Salir")
        print("-" * 40)

        eleccion = input("Seleccione una opción: ").strip()

        if eleccion == '0':
            print("👋 ¡Adiós! Cerrando el programa.")
            break
        elif eleccion in opciones:
            print("-" * 40)
            opciones[eleccion][1]()  # Llama a la función correspondiente
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# --- Ejecución del Programa ---

if __name__ == "__main__":
    # Inicializa la DB al inicio si no existe
    inicializar_db()

    # Ejecuta el menú (Ejercicio 6)
    ejercicio_6_menu_principal()
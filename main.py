import random
def crear_base_clientes():
    clientes = []
    cantidad = int(input("¿Cuántos clientes desea generar?: "))
    for i in range(1, cantidad + 1):
        nombre = input(f"Ingrese el nombre del cliente {i}: ")
        apellido = input(f"Ingrese el apellido del cliente {i}: ")
        saldo = random.randint(500, 1500)
        cliente = {"ID": i, "Nombre": nombre, "Apellido": apellido, "Saldo": saldo}
        clientes.append(cliente)
    return clientes
print(crear_base_clientes())
def mostrar_clientes(clientes):
    print("\n--- LISTA DE CLIENTES ---")
    for x in clientes: print(f"ID: {x['ID']} | Nombre: {x['Nombre']}  Apellido: {x['Apellido']} | Saldo: ${x['Saldo']}")
print(mostrar_clientes())
def buscar_cliente_por_id(clientes):

    buscar_id = int(input("\nIngrese el ID del cliente a buscar: "))
    for a in clientes:
     if a["ID"] == buscar_id:
      print(f"Cliente encontrado: ID: {a['ID']}  Nombre: {a['Nombre']} | Apellido: {a['Apellido']} | Saldo: ${a['Saldo']}")


print(buscar_cliente_por_id())


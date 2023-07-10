import datetime

entradas = {
    "Platinum": {"precio": 120000, "rango": range(1, 21)},
    "Gold": {"precio": 80000, "rango": range(21, 51)},
    "Silver": {"precio": 50000, "rango": range(51, 101)}
}

asientos = ["Disponible" for _ in range(100)]
asistentes = []

def mostrar_menu():
    print("------ Menú ------")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    print("------------------")

def comprar_entradas():
    cantidad = int(input(" Ingrese la cantidad de entradas a comprar (1-3) : "))

    if cantidad < 1 or cantidad > 3:
        print("Cantidad invalida. Intente nuevamente.")
        return

    disponibles = obtener_ubicaciones_disponibles()

    if len(disponibles) < cantidad:
        print("No hay suficientes ubicaciones disponibles.")
        return

    print(" Ubicaciones disponibles : ")
    for i, ubicacion in enumerate(disponibles, start=1):
        print(f"{i}. {ubicacion}")

    compras = []
    for _ in range(cantidad):
        while True:
            opcion = int(input(" Seleccione una ubicación : "))

            if opcion < 1 or opcion > len(disponibles):
                print("Opción inválida. Intente nuevamente.")
                continue

            ubicacion_seleccionada = disponibles[opcion - 1]

            if asientos[ubicacion_seleccionada] != " Disponible ":
                print("La ubicación seleccionada no está disponible. Intente nuevamente.")
                continue

            compras.append(ubicacion_seleccionada)
            break

    run = input(" Ingrese el RUN del asistente (sin guiones, puntos ni digito verificador) : ")
    asistentes.append(run)

    for ubicacion in compras:
        asientos[ubicacion] = run

    print("La operación se ha realizado correctamente.")

def obtener_ubicaciones_disponibles():
    disponibles = []
    for entrada, info in entradas.items():
        for num_asiento in info["rango"]:
            if asientos[num_asiento - 1] == "Disponible":
                disponibles.append(f"{entrada} - Asiento {num_asiento}")
    return disponibles

def mostrar_ubicaciones_disponibles():
    print("Estado actual de las ubicaciones:")
    print("Ubicación\t\tDisponibilidad")
    for i, estado in enumerate(asientos, start=1):
        ubicacion = f"Asiento {i}"
        disponibilidad = "Disponible" if estado == "Disponible" else "Vendido"
        print(f"{ubicacion}\t\t{disponibilidad}")

def ver_listado_asistentes():
    if len(asistentes) == 0:
        print("No hay asistentes registrados.")
        return

    print(" Listado de asistentes por RUN: " )
    for asistente in sorted(asistentes):
        print(asistente)

def mostrar_ganancias_totales():
    total_ganancias = 0
    print("Ganancias totales:")
    print("Tipo de Entrada\t\tCantidad\tTotal")

    for entrada, info in entradas.items():
        cantidad = sum([1 for asiento in asientos if asiento != "Disponible" and asiento in info["rango"]])
        total = cantidad * info["precio"]
        print(f"{entrada}\t\t{cantidad}\t{total}")
        total_ganancias += total

    print(f"TOTAL\t\t\t\t\t\t{total_ganancias}")

while True:
    mostrar_menu()
    opcion = input(" Seleccione una opción : ")

    if opcion == "1":
        comprar_entradas()
    elif opcion == "2":
        mostrar_ubicaciones_disponibles()
    elif opcion == "3":
        ver_listado_asistentes()
    elif opcion == "4":
        mostrar_ganancias_totales()
    elif opcion == "5":
        nombre = input(" Ingrese su nombre : ")
        apellido = input(" Ingrese su apellido : ")
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Saliendo del sistema... {nombre} {apellido} - {fecha_actual}")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

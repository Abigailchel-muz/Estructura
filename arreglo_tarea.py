# Programa de ventas mensuales
# Departamentos: Ropa, Deportes y Juguetería

# Arreglo bidimensional de 12 meses x 3 departamentos
ventas = [
    [0, 0, 0],  # Enero
    [0, 0, 0],  # Febrero
    [0, 0, 0],  # Marzo
    [0, 0, 0],  # Abril
    [0, 0, 0],  # Mayo
    [0, 0, 0],  # Junio
    [0, 0, 0],  # Julio
    [0, 0, 0],  # Agosto
    [0, 0, 0],  # Septiembre
    [0, 0, 0],  # Octubre
    [0, 0, 0],  # Noviembre
    [0, 0, 0]   # Diciembre
]

# Lista de meses
meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]

# Lista de departamentos
departamentos = [
    "Ropa",
    "Deportes",
    "Juguetería"
]


# ---------------------------------------------------
# MÉTODO 1: INSERTAR UNA VENTA
# ---------------------------------------------------

def insertar_venta():
    print("\n--- INSERTAR VENTA ---")

    print("\nMeses:")
    for i in range(len(meses)):
        print(i + 1, "-", meses[i])

    opcion_mes = int(input("Selecciona el número del mes: "))

    if opcion_mes < 1 or opcion_mes > 12:
        print("Mes no válido.")
        return

    print("\nDepartamentos:")
    for i in range(len(departamentos)):
        print(i + 1, "-", departamentos[i])

    opcion_departamento = int(input("Selecciona el departamento: "))

    if opcion_departamento < 1 or opcion_departamento > 3:
        print("Departamento no válido.")
        return

    venta = float(input("Ingresa el valor de la venta: $"))

    # Guardar la venta en el arreglo bidimensional
    ventas[opcion_mes - 1][opcion_departamento - 1] = venta

    print("\nVenta insertada correctamente.")
    print("Mes:", meses[opcion_mes - 1])
    print("Departamento:", departamentos[opcion_departamento - 1])
    print("Venta: $", venta)


# ---------------------------------------------------
# MÉTODO 2: BUSCAR UNA VENTA
# ---------------------------------------------------

def buscar_venta():
    print("\n--- BUSCAR VENTA ---")

    print("\nMeses:")
    for i in range(len(meses)):
        print(i + 1, "-", meses[i])

    opcion_mes = int(input("Selecciona el número del mes: "))

    if opcion_mes < 1 or opcion_mes > 12:
        print("Mes no válido.")
        return

    print("\nDepartamentos:")
    for i in range(len(departamentos)):
        print(i + 1, "-", departamentos[i])

    opcion_departamento = int(input("Selecciona el departamento: "))

    if opcion_departamento < 1 or opcion_departamento > 3:
        print("Departamento no válido.")
        return

    # Buscar el elemento dentro del arreglo
    venta = ventas[opcion_mes - 1][opcion_departamento - 1]

    print("\nResultado de la búsqueda:")
    print("Mes:", meses[opcion_mes - 1])
    print("Departamento:", departamentos[opcion_departamento - 1])
    print("Venta: $", venta)


# ---------------------------------------------------
# MÉTODO 3: ELIMINAR UNA VENTA
# ---------------------------------------------------

def eliminar_venta():
    print("\n--- ELIMINAR VENTA ---")

    print("\nMeses:")
    for i in range(len(meses)):
        print(i + 1, "-", meses[i])

    opcion_mes = int(input("Selecciona el número del mes: "))

    if opcion_mes < 1 or opcion_mes > 12:
        print("Mes no válido.")
        return

    print("\nDepartamentos:")
    for i in range(len(departamentos)):
        print(i + 1, "-", departamentos[i])

    opcion_departamento = int(input("Selecciona el departamento: "))

    if opcion_departamento < 1 or opcion_departamento > 3:
        print("Departamento no válido.")
        return

    # Guardamos el dato antes de eliminarlo
    venta = ventas[opcion_mes - 1][opcion_departamento - 1]

    # Eliminar la venta colocando 0
    ventas[opcion_mes - 1][opcion_departamento - 1] = 0

    print("\nVenta eliminada correctamente.")
    print("Mes:", meses[opcion_mes - 1])
    print("Departamento:", departamentos[opcion_departamento - 1])
    print("Venta eliminada: $", venta)


# ---------------------------------------------------
# MOSTRAR EL ARREGLO BIDIMENSIONAL
# ---------------------------------------------------

def mostrar_ventas():
    print("\n==============================================================")
    print("                    TABLA DE VENTAS")
    print("==============================================================")

    print(f"{'Mes':<15}{'Ropa':>12}{'Deportes':>15}{'Juguetería':>17}")
    print("-" * 59)

    for i in range(12):
        print(
            f"{meses[i]:<15}"
            f"${ventas[i][0]:>11.2f}"
            f"${ventas[i][1]:>14.2f}"
            f"${ventas[i][2]:>16.2f}"
        )

    print("-" * 59)


# ---------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------

while True:

    print("\n========================================")
    print("       SISTEMA DE VENTAS MENSUALES")
    print("========================================")
    print("1. Insertar una venta")
    print("2. Buscar una venta")
    print("3. Eliminar una venta")
    print("4. Mostrar todas las ventas")
    print("5. Salir")
    print("========================================")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        insertar_venta()

    elif opcion == "2":
        buscar_venta()

    elif opcion == "3":
        eliminar_venta()

    elif opcion == "4":
        mostrar_ventas()

    elif opcion == "5":
        print("\nPrograma finalizado.")
        break

    else:
        print("\nOpción no válida. Intenta nuevamente.")
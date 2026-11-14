# Método de ordenamiento: ShellSort

def shell_sort(numeros):
    datos = numeros.copy()
    # ===== INICIO DEL MÉTODO SHELLSORT =====
    salto = len(datos) // 2
    while salto > 0:
        for i in range(salto, len(datos)):
            temporal = datos[i]
            j = i
            while j >= salto and datos[j - salto] > temporal:
                datos[j] = datos[j - salto]
                j -= salto
            datos[j] = temporal
        salto //= 2
    # ===== FIN DEL MÉTODO SHELLSORT =====
    return datos

def leer_cantidad():
    while True:
        try:
            cantidad = int(input("¿Cuántos números deseas ordenar? "))
            if cantidad > 0:
                return cantidad
            print("La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Ingresa un número entero válido.")


def leer_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                valor = int(input(f"Número {i + 1}: "))
                numeros.append(valor)
                break
            except ValueError:
                print("Ingresa un número entero válido.")
    return numeros


def main():
    while True:
        print("\n===== MENÚ: ShellSort =====")
        print("1. Ingresar y ordenar números")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            cantidad = leer_cantidad()
            numeros = leer_numeros(cantidad)
            print("Números originales:", numeros)
            print("Números ordenados:", shell_sort(numeros))
        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()

# Método de ordenamiento: QuickSort

def quick_sort(numeros):
    # ===== INICIO DEL MÉTODO QUICKSORT =====
    if len(numeros) <= 1:
        return numeros.copy()
    pivote = numeros[len(numeros) // 2]
    menores = [x for x in numeros if x < pivote]
    iguales = [x for x in numeros if x == pivote]
    mayores = [x for x in numeros if x > pivote]
    resultado = quick_sort(menores) + iguales + quick_sort(mayores)
    # ===== FIN DEL MÉTODO QUICKSORT =====
    return resultado

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
        print("\n===== MENÚ: QuickSort =====")
        print("1. Ingresar y ordenar números")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            cantidad = leer_cantidad()
            numeros = leer_numeros(cantidad)
            print("Números originales:", numeros)
            print("Números ordenados:", quick_sort(numeros))
        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()

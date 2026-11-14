# Método de ordenamiento: HeapSort

def heap_sort(numeros):
    datos = numeros.copy()
    # ===== INICIO DEL MÉTODO HEAPSORT =====
    def ajustar_monticulo(tamano, raiz):
        mayor = raiz
        izquierda = 2 * raiz + 1
        derecha = 2 * raiz + 2
        if izquierda < tamano and datos[izquierda] > datos[mayor]:
            mayor = izquierda
        if derecha < tamano and datos[derecha] > datos[mayor]:
            mayor = derecha
        if mayor != raiz:
            datos[raiz], datos[mayor] = datos[mayor], datos[raiz]
            ajustar_monticulo(tamano, mayor)

    n = len(datos)
    for i in range(n // 2 - 1, -1, -1):
        ajustar_monticulo(n, i)
    for fin in range(n - 1, 0, -1):
        datos[0], datos[fin] = datos[fin], datos[0]
        ajustar_monticulo(fin, 0)
    # ===== FIN DEL MÉTODO HEAPSORT =====
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
        print("\n===== MENÚ: HeapSort =====")
        print("1. Ingresar y ordenar números")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            cantidad = leer_cantidad()
            numeros = leer_numeros(cantidad)
            print("Números originales:", numeros)
            print("Números ordenados:", heap_sort(numeros))
        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()

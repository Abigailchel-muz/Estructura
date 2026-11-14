# Método de ordenamiento: RadixSort

def radix_sort(numeros):
    datos = numeros.copy()
    # ===== INICIO DEL MÉTODO RADIX SORT =====
    def ordenar_no_negativos(valores):
        if not valores:
            return []
        resultado = valores.copy()
        maximo = max(resultado)
        posicion = 1
        while maximo // posicion > 0:
            grupos = [[] for _ in range(10)]
            for numero in resultado:
                digito = (numero // posicion) % 10
                grupos[digito].append(numero)
            resultado = [numero for grupo in grupos for numero in grupo]
            posicion *= 10
        return resultado

    negativos = [-x for x in datos if x < 0]
    positivos = [x for x in datos if x >= 0]
    negativos_ordenados = ordenar_no_negativos(negativos)
    positivos_ordenados = ordenar_no_negativos(positivos)
    resultado = [-x for x in reversed(negativos_ordenados)] + positivos_ordenados
    # ===== FIN DEL MÉTODO RADIX SORT =====
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
        print("\n===== MENÚ: RadixSort =====")
        print("1. Ingresar y ordenar números")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            cantidad = leer_cantidad()
            numeros = leer_numeros(cantidad)
            print("Números originales:", numeros)
            print("Números ordenados:", radix_sort(numeros))
        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()

def mostrar_vector(datos):
    for dato in datos:
        print(dato)


def media(datos):
    suma = 0

    for dato in datos:
        suma = suma + dato

    return suma / len(datos)


def main():
    pares = [2, 4, 6, 8, 10]
    impares = [1, 3, 5, 7, 9]

    mostrar_vector(pares)
    print("Media =", media(pares))

    mostrar_vector(impares)
    print("Media =", media(impares))


main()
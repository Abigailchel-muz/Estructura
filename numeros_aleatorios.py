import random
import statistics


def main():
    # Generar 50 números aleatorios entre 1 y 100
    datos = [random.randint(150, 250) for _ in range(50)]

    print("Lista de números:")
    print(datos)

    # Media
    media = statistics.mean(datos)

    # Moda
    moda = statistics.multimode(datos)

    # Mediana
    mediana = statistics.median(datos)

    # Desviación estándar
    desviacion = statistics.pstdev(datos)

    # Varianza
    varianza = statistics.pvariance(datos)

    print("\nResultados:")
    print("Media =", media)
    print("Moda =", moda)
    print("Mediana =", mediana)
    print("Desviación estándar =", desviacion)
    print("Varianza =", varianza)


main()
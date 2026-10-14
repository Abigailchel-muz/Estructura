"""Torre de Hanoi en Python: solución recursiva con medición de tiempo."""
import sys
import time


def hanoi(n, origen, destino, auxiliar, contador):
    """Resuelve recursivamente la Torre de Hanoi.
    contador es una lista de 1 elemento que acumula los movimientos."""
    if n == 0:
        return
    hanoi(n - 1, origen, auxiliar, destino, contador)
    contador[0] += 1  # aquí se "movería" el disco n de origen a destino
    hanoi(n - 1, auxiliar, destino, origen, contador)


def resolver(n):
    """Prepara la solución para n discos y devuelve el total de movimientos."""
    contador = [0]
    hanoi(n, "A", "C", "B", contador)
    return contador[0]


def medir_tiempo(n):
    """Mide el tiempo (segundos) que tarda en resolver n discos."""
    inicio = time.perf_counter()
    movimientos = resolver(n)
    fin = time.perf_counter()
    return movimientos, fin - inicio


def main():
    sys.setrecursionlimit(10000)
    discos = [int(a) for a in sys.argv[1:]] or [5, 10, 30]
    print(f"{'Discos':>7} | {'Movimientos':>26} | {'Tiempo (s)':>12}")
    print("-" * 52)
    for n in discos:
        mov, t = medir_tiempo(n)
        print(f"{n:>7} | {mov:>26,} | {t:>12.6f}", flush=True)


if __name__ == "__main__":
    main()
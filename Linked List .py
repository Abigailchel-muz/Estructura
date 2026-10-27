class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None


def dibujar(inicio, marcas=None):
    """Dibuja la lista desde 'inicio' y pone los apuntadores debajo de cada nodo."""
    marcas = marcas or {}
    linea, marcador = "", ""
    t = inicio
    while t is not None:
        celda = f"[{t.info}]"
        etiquetas = ",".join(n for n, nodo in marcas.items() if nodo is t)
        linea += celda + " -> "
        marcador += ("^" + etiquetas if etiquetas else "").ljust(len(celda) + 4)
        t = t.liga
    linea += "NIL"
    print("     " + linea)
    if marcador.strip():
        print("     " + marcador)


class ListaSimple:
    def __init__(self):
        self.p = None

    # ---------- INSERTAR AL INICIO ----------
    def insertar_inicio(self, info):
        print("\n  Antes:")
        dibujar(self.p, {"P": self.p})

        q = Nodo(info)
        print(f"\n  1) Crear(Q) y leer INFO  ->  Q = [{info}] -> NIL")

        q.liga = self.p
        print("  2) Q.LIGA <- P  (Q apunta al antiguo primer nodo)")
        dibujar(q, {"Q": q, "P": self.p})

        self.p = q
        print("  3) P <- Q  (P ahora apunta al nuevo primer nodo)")

        print("\n  Después:")
        dibujar(self.p, {"P": self.p})

    # ---------- INSERTAR AL FINAL ----------
    def insertar_final(self, info):
        print("\n  Antes:")
        dibujar(self.p, {"P": self.p})

        q = Nodo(info)
        print(f"\n  1) Crear(Q) y leer INFO  ->  Q = [{info}] -> NIL")

        if self.p is None:
            self.p = q
            print("  2) La lista estaba vacía: P <- Q")
        else:
            t = self.p
            print("  2) T <- P  (T recorrerá la lista hasta el último nodo)")
            dibujar(self.p, {"T": t})
            while t.liga is not None:
                t = t.liga
                print("     T <- T.LIGA")
                dibujar(self.p, {"T": t})
            t.liga = q
            print("  3) T.LIGA <- Q  (el último nodo ahora apunta a Q)")

        print("\n  Después:")
        dibujar(self.p, {"P": self.p})

    # ---------- ELIMINAR AL INICIO ----------
    def eliminar_inicio(self):
        if self.p is None:
            return None
        print("\n  Antes:")
        dibujar(self.p, {"P": self.p})

        q = self.p
        print("\n  1) Q <- P  (Q marca el nodo a eliminar)")
        dibujar(self.p, {"P": self.p, "Q": q})

        self.p = q.liga
        print("  2) P <- P.LIGA  (P avanza al segundo nodo)")
        dibujar(q, {"Q": q, "P": self.p})

        q.liga = None
        print("  3) Q.LIGA <- NIL y se libera Q")

        print("\n  Después:")
        dibujar(self.p, {"P": self.p})
        return q.info

    # ---------- ELIMINAR AL FINAL ----------
    def eliminar_final(self):
        if self.p is None:
            return None
        print("\n  Antes:")
        dibujar(self.p, {"P": self.p})

        if self.p.liga is None:
            info = self.p.info
            print("\n  1) Solo hay un nodo: P <- NIL")
            self.p = None
        else:
            ant = self.p
            print("\n  1) ANT <- P  (ANT buscará el penúltimo nodo)")
            dibujar(self.p, {"ANT": ant})
            while ant.liga.liga is not None:
                ant = ant.liga
                print("     ANT <- ANT.LIGA")
                dibujar(self.p, {"ANT": ant})
            ult = ant.liga
            info = ult.info
            print("  2) ANT es el penúltimo; ULT es el último nodo")
            dibujar(self.p, {"ANT": ant, "ULT": ult})
            ant.liga = None
            print("  3) ANT.LIGA <- NIL  (se desconecta el último nodo)")

        print("\n  Después:")
        dibujar(self.p, {"P": self.p})
        return info

    # ---------- BUSCAR ----------
    def buscar(self, x):
        print(f"\n  Buscando '{x}':")
        if self.p is None:
            print("  La lista está vacía.")
            return None

        t = self.p
        pos = 1
        print("  1) T <- P  (T recorrerá la lista comparando INFO)")
        dibujar(self.p, {"T": t})

        while t is not None and t.info != x:
            print(f"     T.INFO = '{t.info}' ≠ '{x}'  ->  T <- T.LIGA")
            t = t.liga
            pos += 1
            if t is not None:
                dibujar(self.p, {"T": t})

        if t is None:
            print("     T <- NIL  (se llegó al final de la lista)")
            print(f"  Resultado: '{x}' NO se encontró en la lista.")
            return None

        print(f"     T.INFO = '{t.info}' = '{x}'  ->  ¡encontrado!")
        dibujar(self.p, {"T": t})
        print(f"  Resultado: '{x}' se encontró en la posición {pos}.")
        return pos


def menu(lista):
    print("\n" + "=" * 44)
    print("  LISTA ACTUAL")
    print("=" * 44)
    dibujar(lista.p, {"P": lista.p})
    print("-" * 44)
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Eliminar al inicio")
    print("4. Eliminar al final")
    print("5. Buscar un valor")
    print("0. Salir")
    return input("Elige una opción: ")


if __name__ == "__main__":
    lista = ListaSimple()

    while True:
        opcion = menu(lista)

        if opcion == "1":
            lista.insertar_inicio(input("Valor a insertar al inicio: "))
        elif opcion == "2":
            lista.insertar_final(input("Valor a insertar al final: "))
        elif opcion == "3":
            if lista.eliminar_inicio() is None:
                print("La lista está vacía.")
        elif opcion == "4":
            if lista.eliminar_final() is None:
                print("La lista está vacía.")
        elif opcion == "5":
            lista.buscar(input("Valor a buscar: "))
        elif opcion == "0":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida.")
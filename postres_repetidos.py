"""
Ejercicio 2 - Eliminar automaticamente los elementos repetidos de POSTRES
----------------------------------------------------------------------
Arreglo (lista de Python) ordenado alfabéticamente. Cada elemento guarda el
nombre de un postre y la cabeza de una lista ligada con sus ingredientes.

    POSTRES[i] = [nombre, cabeza]  ->  [ing1|*] -> [ing2|*] -> ... -> NIL
"""
import sys


class Nodo:
    """Nodo de la lista ligada de ingredientes."""
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente
        self.siguiente = None          # NIL


POSTRES = []                           # arreglo ordenado alfabéticamente


POSTRES = []                           # arreglo ordenado alfabéticamente


def norm(texto):
    """Normaliza para comparar (sin espacios extra y sin distinguir mayúsculas)."""
    return " ".join(texto.split()).lower()


def existe_ingrediente(cabeza, ingrediente):
    clave = norm(ingrediente)
    while cabeza is not None:
        if norm(cabeza.ingrediente) == clave:
            return True
        cabeza = cabeza.siguiente
    return False


def agregar_al_final(cabeza, ingrediente):
    """Agrega un nodo al final de la lista y regresa la cabeza."""
    nuevo = Nodo(ingrediente)
    if cabeza is None:
        return nuevo
    aux = cabeza
    while aux.siguiente is not None:
        aux = aux.siguiente
    aux.siguiente = nuevo
    return cabeza


def construir_lista(ingredientes):
    """Crea una lista ligada sin ingredientes vacíos ni repetidos."""
    cabeza = None
    for ing in ingredientes:
        ing = " ".join(ing.split())
        if ing and not existe_ingrediente(cabeza, ing):
            cabeza = agregar_al_final(cabeza, ing)
    return cabeza


def lista_a_python(cabeza):
    salida = []
    while cabeza is not None:
        salida.append(cabeza.ingrediente)
        cabeza = cabeza.siguiente
    return salida


# ------------------------------------------------------- ejercicio 2
def eliminar_repetidos():
    """
    Elimina automáticamente los postres repetidos de POSTRES.
    Como el arreglo está ordenado, los repetidos son consecutivos: basta una
    sola pasada. Se conserva la primera aparición; la lista ligada del
    elemento repetido se descarta junto con él.
    """
    eliminados = 0
    i = 0
    while i < len(POSTRES) - 1:
        if norm(POSTRES[i][0]) == norm(POSTRES[i + 1][0]):
            print(f"Repetido: '{POSTRES[i + 1][0]}' (posición {i + 1}) "
                  f"-> se elimina con su lista "
                  f"{lista_a_python(POSTRES[i + 1][1])}")
            POSTRES.pop(i + 1)
            eliminados += 1
        else:
            i += 1
    print(f"Elementos repetidos eliminados: {eliminados}")
    return eliminados


def mostrar_todo():
    if not POSTRES:
        print("POSTRES = []")
    for i, (nom, cab) in enumerate(POSTRES):
        print(f"[{i}] {nom}: {' -> '.join(lista_a_python(cab))} -> NIL")


# ------------------------------------------------------------------- pruebas
def demo():
    # Datos con repetidos cargados directamente en el arreglo (ordenado).
    POSTRES.extend([
        ["Brownie", construir_lista(["chocolate", "nuez"])],
        ["Flan", construir_lista(["leche", "huevo"])],
        ["Flan", construir_lista(["leche", "caramelo"])],
        ["Flan", construir_lista(["vainilla"])],
        ["Gelatina", construir_lista(["grenetina", "agua"])],
        ["Gelatina", construir_lista(["agua"])],
    ])
    print("Antes:")
    mostrar_todo()
    eliminar_repetidos()
    print("Despues:")
    mostrar_todo()
    print("\nSin repetidos (segunda llamada):")
    eliminar_repetidos()
    POSTRES.clear()
    print("Arreglo vacio:")
    eliminar_repetidos()


if __name__ == "__main__":
    demo()
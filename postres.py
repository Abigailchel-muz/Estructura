"""
Ejercicio 1 - Estructura de datos POSTRES (incisos a, b, c, d, e)
--------------------------------------------------------------
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


# ----------------------------------------------------------------- utilidades
def norm(texto):
    """Normaliza para comparar (sin espacios extra y sin distinguir mayúsculas)."""
    return " ".join(texto.split()).lower()


def buscar_postre(nombre):
    """Búsqueda binaria. Regresa (encontrado, posición donde está / debe ir)."""
    clave = norm(nombre)
    izq, der = 0, len(POSTRES) - 1
    while izq <= der:
        medio = (izq + der) // 2
        actual = norm(POSTRES[medio][0])
        if actual == clave:
            return True, medio
        if actual < clave:
            izq = medio + 1
        else:
            der = medio - 1
    return False, izq


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


# ------------------------------------------------------------------ inciso a
def imprimir_ingredientes(nombre):
    """a) Dado el nombre de un postre, imprime todos sus ingredientes."""
    if not POSTRES:
        print("El arreglo POSTRES está vacío.")
        return False
    if not norm(nombre):
        print("Error: el nombre del postre no puede estar vacío.")
        return False
    ok, pos = buscar_postre(nombre)
    if not ok:
        print(f"El postre '{nombre}' no existe.")
        return False
    cabeza = POSTRES[pos][1]
    if cabeza is None:
        print(f"'{POSTRES[pos][0]}' no tiene ingredientes registrados.")
        return True
    print(f"Ingredientes de '{POSTRES[pos][0]}':")
    i = 1
    while cabeza is not None:
        print(f"  {i}. {cabeza.ingrediente}")
        cabeza, i = cabeza.siguiente, i + 1
    return True


# ------------------------------------------------------------------ inciso b
def insertar_ingredientes(nombre, nuevos):
    """b) Inserta nuevos ingredientes en la lista del postre indicado."""
    if not POSTRES:
        print("El arreglo POSTRES está vacío; primero dé de alta un postre.")
        return False
    ok, pos = buscar_postre(nombre)
    if not ok:
        print(f"El postre '{nombre}' no existe.")
        return False
    if not nuevos:
        print("No se indicó ningún ingrediente.")
        return False
    for ing in nuevos:
        ing = " ".join(ing.split())
        if not ing:
            print("  - Ingrediente vacío: se omite.")
        elif existe_ingrediente(POSTRES[pos][1], ing):
            print(f"  - '{ing}' ya existe en la lista: se omite.")
        else:
            POSTRES[pos][1] = agregar_al_final(POSTRES[pos][1], ing)
            print(f"  + '{ing}' insertado.")
    return True


# ------------------------------------------------------------------ inciso c
def eliminar_ingrediente(nombre, ingrediente):
    """c) Elimina un ingrediente de la lista del postre indicado."""
    if not POSTRES:
        print("El arreglo POSTRES está vacío.")
        return False
    ok, pos = buscar_postre(nombre)
    if not ok:
        print(f"El postre '{nombre}' no existe.")
        return False
    cabeza = POSTRES[pos][1]
    if cabeza is None:
        print(f"'{POSTRES[pos][0]}' no tiene ingredientes que eliminar.")
        return False
    clave = norm(ingrediente)
    if norm(cabeza.ingrediente) == clave:            # caso: es el primero
        POSTRES[pos][1] = cabeza.siguiente
        print(f"'{ingrediente}' eliminado (era el primero).")
        return True
    ant, act = cabeza, cabeza.siguiente
    while act is not None:                           # caso: medio o final
        if norm(act.ingrediente) == clave:
            ant.siguiente = act.siguiente
            print(f"'{ingrediente}' eliminado.")
            return True
        ant, act = act, act.siguiente
    print(f"'{ingrediente}' no está en la lista de '{POSTRES[pos][0]}'.")
    return False


# ------------------------------------------------------------------ inciso d
def alta_postre(nombre, ingredientes):
    """d) Da de alta un postre (en su lugar alfabético) con sus ingredientes."""
    nombre = " ".join(nombre.split())
    if not nombre:
        print("Error: el nombre del postre no puede estar vacío.")
        return False
    ok, pos = buscar_postre(nombre)
    if ok:
        print(f"El postre '{nombre}' ya existe; no se duplica.")
        return False
    POSTRES.insert(pos, [nombre, construir_lista(ingredientes)])
    print(f"Postre '{nombre}' dado de alta en la posición {pos}.")
    return True


# ------------------------------------------------------------------ inciso e
def baja_postre(nombre):
    """e) Da de baja un postre junto con toda su lista de ingredientes."""
    if not POSTRES:
        print("El arreglo POSTRES está vacío.")
        return False
    ok, pos = buscar_postre(nombre)
    if not ok:
        print(f"El postre '{nombre}' no existe.")
        return False
    POSTRES.pop(pos)       # al perder la referencia, la lista queda liberada
    print(f"Postre '{nombre}' dado de baja junto con sus ingredientes.")
    return True


def mostrar_todo():
    if not POSTRES:
        print("POSTRES = []")
    for i, (nom, cab) in enumerate(POSTRES):
        print(f"[{i}] {nom}: {' -> '.join(lista_a_python(cab))} -> NIL")


# ------------------------------------------------------------------- pruebas
def demo():
    print("=== d) Alta de postres ===")
    alta_postre("Pastel de chocolate", ["harina", "cacao", "huevo", "azúcar"])
    alta_postre("Flan", ["leche", "huevo", "azúcar", "vainilla"])
    alta_postre("Arroz con leche", ["arroz", "leche", "canela", "azúcar"])
    alta_postre("flan", ["leche"])            # repetido
    alta_postre("   ", ["x"])                 # vacío
    mostrar_todo()
    print("\n=== a) Imprimir ingredientes ===")
    imprimir_ingredientes("Flan")
    imprimir_ingredientes("Gelatina")         # no existe
    print("\n=== b) Insertar ingredientes ===")
    insertar_ingredientes("Flan", ["caramelo", "huevo", ""])
    insertar_ingredientes("Gelatina", ["agua"])
    imprimir_ingredientes("Flan")
    print("\n=== c) Eliminar ingrediente ===")
    eliminar_ingrediente("Flan", "leche")     # primero
    eliminar_ingrediente("Flan", "caramelo")  # último
    eliminar_ingrediente("Flan", "sal")       # no existe
    eliminar_ingrediente("Gelatina", "agua")  # postre no existe
    mostrar_todo()
    print("\n=== e) Baja de postre ===")
    baja_postre("Arroz con leche")
    baja_postre("Arroz con leche")            # ya no existe
    mostrar_todo()


# ---------------------------------------------------------------------- menú
def menu():
    ops = """
1) Imprimir ingredientes de un postre
2) Insertar ingredientes a un postre
3) Eliminar un ingrediente de un postre
4) Dar de alta un postre
5) Dar de baja un postre
6) Mostrar todo
0) Salir"""
    while True:
        print(ops)
        op = input("Opción: ").strip()
        if op == "0":
            break
        elif op == "1":
            imprimir_ingredientes(input("Postre: "))
        elif op == "2":
            n = input("Postre: ")
            insertar_ingredientes(n, input("Ingredientes (separados por coma): ").split(","))
        elif op == "3":
            eliminar_ingrediente(input("Postre: "), input("Ingrediente: "))
        elif op == "4":
            n = input("Postre: ")
            alta_postre(n, input("Ingredientes (separados por coma): ").split(","))
        elif op == "5":
            baja_postre(input("Postre: "))
        elif op == "6":
            mostrar_todo()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    demo() if "--demo" in sys.argv else menu()
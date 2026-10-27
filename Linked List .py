class Elemento:
    def __init__(self, valor):
        self.valor = valor      # Campo de datos del elemento
        self.enlace = None      # Enlace al siguiente (inicialmente None)


# --- Agregar_frente ---
def agregar_frente(cabeza, nuevo_valor):
    """Agrega un elemento al frente de una lista simplemente enlazada."""
    nuevo = Elemento(nuevo_valor)
    nuevo.enlace = cabeza
    cabeza = nuevo
    return cabeza


# --- Construir_lista ---
def construir_lista():
    print("--- Construcción de la Lista (Construir_lista) ---")
    cabeza = None

    primer_valor = input("Escriba el valor del primer elemento: ")
    cabeza = Elemento(primer_valor)
    cabeza.enlace = None

    continuar = int(input("¿Quiere agregar más elementos? Sí: 1, No: 0: "))

    while continuar == 1:
        valor = input("Escriba el valor del nuevo elemento: ")
        cabeza = agregar_frente(cabeza, valor)
        continuar = int(input("¿Quiere agregar más elementos? Sí: 1, No: 0: "))

    return cabeza


# --- Localizar_recursivo ---
def localizar_recursivo(cabeza, objetivo):
    """Localiza recursivamente un elemento con valor 'objetivo' en la lista."""
    if cabeza is not None:
        if cabeza.valor == objetivo:
            print("El valor sí está en la lista")
            return True
        else:
            return localizar_recursivo(cabeza.enlace, objetivo)
    else:
        print("El valor no está en la lista")
        return False


# --- Función para Borrar un Elemento ---
def borrar_elemento(cabeza, objetivo):
    """Borra la primera aparición de un elemento con valor 'objetivo'."""
    if cabeza is None:
        print("La lista no tiene elementos.")
        return cabeza

    # Si el elemento a borrar es el primero
    if cabeza.valor == objetivo:
        print(f"Valor '{objetivo}' borrado del frente.")
        return cabeza.enlace  # La nueva cabeza es el siguiente elemento

    cursor = cabeza
    while cursor.enlace is not None and cursor.enlace.valor != objetivo:
        cursor = cursor.enlace

    # Si el valor está en el elemento siguiente al cursor
    if cursor.enlace is not None:
        cursor.enlace = cursor.enlace.enlace  # Se salta el elemento a borrar
        print(f"Valor '{objetivo}' borrado con éxito.")
    else:
        print(f"El valor '{objetivo}' no está en la lista, no se puede borrar.")

    return cabeza


# --- Función auxiliar para mostrar la lista ---
def mostrar_lista(cabeza, titulo="\nLista en este momento (de inicio a fin):"):
    cursor = cabeza
    print(titulo)
    if cursor is None:
        print("NIL (Lista vacía)")
        return
    while cursor is not None:
        print(f"[{cursor.valor}] -> ", end="")
        cursor = cursor.enlace
    print("NIL")


# --- Programa Principal ---
if __name__ == "__main__":
    # 1. Construimos la lista
    lista = construir_lista()
    mostrar_lista(lista)

    # 2. Probar Localización
    print("\n--- Localizar en la Lista ---")
    valor_buscado = input("Escriba el valor a localizar: ")
    localizar_recursivo(lista, valor_buscado)

    # 3. Probar Inserción de un nuevo valor al frente
    print("\n--- Agregar un nuevo valor ---")
    valor_nuevo = input("Escriba el valor a agregar al frente: ")
    lista = agregar_frente(lista, valor_nuevo)
    mostrar_lista(lista)

    # 4. Probar Borrado de un valor
    print("\n--- Borrar un valor ---")
    valor_borrar = input("Escriba el valor que quiere borrar: ")
    lista = borrar_elemento(lista, valor_borrar)
    mostrar_lista(lista)

    # 5. Demostración de dos elementos distintos enlazados a un mismo elemento
    print("\n--- Demostración: Dos elementos distintos enlazados a uno solo ---")

    # Creamos el elemento compartido
    elemento_compartido = Elemento("Compartido")
    elemento_compartido.enlace = None

    # Creamos dos elementos independientes
    izquierdo = Elemento("Izquierdo")
    derecho = Elemento("Derecho")

    # Ambos enlaces apuntan exactamente al mismo elemento compartido
    izquierdo.enlace = elemento_compartido
    derecho.enlace = elemento_compartido

    mostrar_lista(izquierdo, "\nRecorriendo desde Izquierdo:")
    mostrar_lista(derecho, "Recorriendo desde Derecho:")

    if izquierdo.enlace is derecho.enlace:
        print("\n¡Comprobado! Los enlaces de 'Izquierdo' y 'Derecho' apuntan al mismo objeto en memoria.")

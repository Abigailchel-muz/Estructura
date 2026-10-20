class Cola:
    """Cola (FIFO) implementada con una lista."""

    def __init__(self):
        self.items = []

    def encolar(self, dato):
        self.items.append(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.items.pop(0)

    def frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.items[0]

    def esta_vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def sumar_colas(cola_a, cola_b):
    """Devuelve una nueva Cola con los elementos de A y B sumados uno a uno.
    No modifica las colas originales."""
    resultado = Cola()
    aux_a, aux_b = Cola(), Cola()

    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        a = cola_a.desencolar()
        b = cola_b.desencolar()
        resultado.encolar(a + b)
        aux_a.encolar(a)
        aux_b.encolar(b)

    # Restaurar las colas originales
    while not aux_a.esta_vacia():
        cola_a.encolar(aux_a.desencolar())
    while not aux_b.esta_vacia():
        cola_b.encolar(aux_b.desencolar())

    return resultado


if __name__ == "__main__":
    cola_a, cola_b = Cola(), Cola()
    for x in [3, 4, 2, 8, 12]:
        cola_a.encolar(x)
    for x in [6, 2, 9, 11, 3]:
        cola_b.encolar(x)

    print("Cola A:", cola_a)
    print("Cola B:", cola_b)
    print("Cola Resultado:", sumar_colas(cola_a, cola_b))
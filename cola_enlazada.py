"""
Práctica 1.2 - Implementación de una cola con listas enlazadas (FIFO)
Estructura: Order, Node, QueueInterface, Queue y prueba en main.
"""
from abc import ABC, abstractmethod


class Order:
    """Representa un pedido: cliente y cantidad de producto."""

    def __init__(self, qtty, customer):
        self._customer = customer
        self._qtty = qtty

    def print(self):
        print(f"  Customer: {self.get_customer()}")
        print(f"  Quantity: {self.get_qtty()}")
        print("  ------------")

    def get_qtty(self):
        return self._qtty

    def get_customer(self):
        return self._customer


class Node:
    """Nodo de la lista enlazada: guarda un objeto (info) y la referencia al siguiente."""

    def __init__(self, info, next_node=None):
        self._info = info
        self._next = next_node

    def get_info(self):
        return self._info

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node


class QueueInterface(ABC):
    @abstractmethod
    def size(self):
        """Devuelve el número de elementos de la cola."""

    @abstractmethod
    def is_empty(self):
        """True si la cola está vacía, False en caso contrario."""

    @abstractmethod
    def front(self):
        """Devuelve el primer elemento SIN extraerlo (None si está vacía)."""

    @abstractmethod
    def enqueue(self, info):
        """Añade un nuevo elemento al final de la cola."""

    @abstractmethod
    def dequeue(self):
        """Devuelve el primer elemento y lo extrae (None si está vacía)."""


class Queue(QueueInterface):
    """Cola FIFO basada en lista enlazada.
    top  -> cabeza de la cola (por donde se extrae)
    tail -> último nodo (por donde se inserta), evita recorrer la lista."""

    def __init__(self):
        self._top = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            return None
        return self._top.get_info()

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self._top = new_node          # primer elemento: top y tail coinciden
        else:
            self._tail.set_next(new_node)  # enlaza tras el último nodo
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self._top.get_info()
        self._top = self._top.get_next()   # desenlaza la cabeza
        self._size -= 1
        if self._top is None:              # la cola quedó vacía
            self._tail = None
        return info

    def get_nth(self, pos):
        """Devuelve el n-ésimo elemento (empezando en 1) sin borrarlo.
        Devuelve None si la posición no es válida."""
        if pos < 1 or pos > self._size:
            return None
        node = self._top
        for _ in range(pos - 1):
            node = node.get_next()
        return node.get_info()

    def print_info(self):
        """Muestra el tamaño y recorre la cola imprimiendo cada elemento."""
        print("********* QUEUE DUMP *********")
        print(f"Size: {self._size}")
        node = self._top
        i = 1
        while node is not None:
            print(f"** Element {i}")
            node.get_info().print()        # usa Order.print()
            node = node.get_next()
            i += 1
        print("******************************")


class TestQueue:
    @staticmethod
    def main():
        queue = Queue()

        print(">> Cola vacía: front =", queue.front(), "| dequeue =", queue.dequeue())
        queue.print_info()

        print("\n>> Encolando 4 pedidos")
        for qtty, customer in [(20, "cust1"), (30, "cust2"), (40, "cust3"), (50, "cust3")]:
            queue.enqueue(Order(qtty, customer))
            queue.print_info()

        print("\n>> front() (no extrae)")
        queue.front().print()
        queue.print_info()

        print("\n>> get_nth(3) (no extrae)")
        queue.get_nth(3).print()
        print("get_nth(0) =", queue.get_nth(0), "| get_nth(9) =", queue.get_nth(9))

        print("\n>> dequeue() (extrae)")
        queue.dequeue().print()
        queue.print_info()

        print("\n>> Vaciando la cola")
        while not queue.is_empty():
            queue.dequeue()
            queue.print_info()


if __name__ == "__main__":
    TestQueue.main()
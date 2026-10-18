class Pila:
    """Implementación clásica de una Pila (LIFO)"""
    def __init__(self):
        self.__items = []

    def push(self, item):
        """Agrega un elemento a la cima de la pila."""
        self.__items.append(item)

    def pop(self):
        """Remueve y devuelve el elemento de la cima."""
        if self.is_empty():
            raise IndexError("La pila está vacía.")
        return self.__items.pop()

    def peek(self):
        """Devuelve el elemento de la cima sin removerlo."""
        if self.is_empty():
            return None
        return self.__items[-1]

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.__items) == 0

    def size(self):
        """Devuelve la cantidad de elementos en la pila."""
        return len(self.__items)

    def obtener_elementos(self):
        """Devuelve una copia de la lista de elementos (de abajo hacia arriba)."""
        return list(self.__items)


class NavegadorWeb:
    """Simulador de historial de navegador utilizando dos pilas"""
    def __init__(self):
        self.pila_atras = Pila()
        self.pila_adelante = Pila()
        self.pagina_actual = None

    def visitar_pagina(self, url):
        """Visita una nueva página web."""
        if self.pagina_actual is not None:
            # Guardamos la página actual en el historial de atrás
            self.pila_atras.push(self.pagina_actual)
        
        self.pagina_actual = url
        
        # Al visitar una nueva página, el historial de "adelante" se limpia
        self.pila_adelante = Pila()
        print(f"➜ Visitando: {self.pagina_actual}")

    def retroceder(self):
        """Vuelve a la página anterior."""
        if self.pila_atras.is_empty():
            print("⚠️ No hay páginas anteriores en el historial.")
            return

        # Guardamos la página actual en la pila de "adelante"
        self.pila_adelante.push(self.pagina_actual)
        
        # Recuperamos la página anterior
        self.pagina_actual = self.pila_atras.pop()
        print(f"⬅️ Retrocedido a: {self.pagina_actual}")

    def avanzar(self):
        """Avanza a la página siguiente (si previamente retrocedimos)."""
        if self.pila_adelante.is_empty():
            print("⚠️ No hay páginas siguientes en el historial.")
            return

        # Guardamos la página actual en la pila de "atrás"
        self.pila_atras.push(self.pagina_actual)
        
        # Recuperamos la página de la pila de "adelante"
        self.pagina_actual = self.pila_adelante.pop()
        print(f"➡️ Avanzado a: {self.pagina_actual}")

    def mostrar_estado(self):
        """Muestra la página actual y el estado de los historiales."""
        print("\n--- Estado del Navegador ---")
        print(f"Página actual : {self.pagina_actual if self.pagina_actual else 'Ninguna'}")
        print(f"Historial Atrás: {self.pila_atras.obtener_elementos()}")
        print(f"Historial Adelante: {self.pila_adelante.obtener_elementos()}")
        print("----------------------------\n")


# ==========================================
# Ejemplos de uso / Demostración
# ==========================================
if __name__ == "__main__":
    navegador = NavegadorWeb()

    # 1. Navegación inicial
    navegador.visitar_pagina("google.com")
    navegador.visitar_pagina("github.com")
    navegador.visitar_pagina("python.org")
    navegador.mostrar_estado()

    # 2. Retroceder páginas
    navegador.retroceder()
    navegador.retroceder()
    navegador.mostrar_estado()

    # 3. Avanzar página
    navegador.avanzar()
    navegador.mostrar_estado()

    # 4. Visitar un nuevo sitio borra el historial de "adelante"
    navegador.visitar_pagina("wikipedia.org")
    navegador.mostrar_estado()
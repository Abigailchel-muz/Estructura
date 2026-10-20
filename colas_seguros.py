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

    def esta_vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)


class SistemaSeguros:
    """Maneja una cola por servicio. Cada servicio tiene su propio
    contador de turnos y su propia Cola de clientes en espera."""

    SERVICIOS = {
        1: "Contratar un seguro",
        2: "Reportar un siniestro",
        3: "Pagos y renovaciones",
        4: "Consultas y aclaraciones",
    }

    def __init__(self):
        self.colas = {s: Cola() for s in self.SERVICIOS}
        self.contadores = {s: 0 for s in self.SERVICIOS}

    def llegada_cliente(self, servicio):
        """Entrega un número de atención para el servicio indicado."""
        if servicio not in self.colas:
            return "Servicio inválido."
        self.contadores[servicio] += 1
        numero = self.contadores[servicio]
        self.colas[servicio].encolar(numero)
        return f"Su número de atención es: S{servicio}-{numero:03d}"

    def atender_cliente(self, servicio):
        """Llama al siguiente cliente de la cola del servicio."""
        if servicio not in self.colas:
            return "Servicio inválido."
        if self.colas[servicio].esta_vacia():
            return f"No hay clientes en espera en el servicio {servicio}."
        numero = self.colas[servicio].desencolar()
        return f"Llamando al número: S{servicio}-{numero:03d}"

    def estado(self):
        lineas = ["--- Clientes en espera ---"]
        for s, nombre in self.SERVICIOS.items():
            lineas.append(f"  Servicio {s} ({nombre}): {self.colas[s].tamanio()}")
        return "\n".join(lineas)


def mostrar_menu(sistema):
    print("=== Compañía de Seguros ===")
    for s, nombre in sistema.SERVICIOS.items():
        print(f"  {s}. {nombre}")
    print("Comandos: C<servicio> = llega cliente | A<servicio> = atender | E = estado | S = salir")
    print("Ejemplo: C1 (llega cliente al servicio 1), A1 (atender servicio 1)\n")


def main():
    sistema = SistemaSeguros()
    mostrar_menu(sistema)

    while True:
        entrada = input("> ").strip().upper()
        if not entrada:
            continue
        if entrada == "S":
            print("Hasta luego.")
            break
        if entrada == "E":
            print(sistema.estado())
            continue

        letra, resto = entrada[0], entrada[1:].strip()
        if letra not in ("C", "A") or not resto.isdigit():
            print("Comando inválido. Use C<n>, A<n>, E o S.")
            continue

        servicio = int(resto)
        if letra == "C":
            print(sistema.llegada_cliente(servicio))
        else:
            print(sistema.atender_cliente(servicio))


if __name__ == "__main__":
    main()
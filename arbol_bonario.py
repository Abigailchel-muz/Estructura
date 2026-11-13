import tkinter as tk
from tkinter import ttk, messagebox


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return True
        actual = self.raiz
        while True:
            if valor == actual.valor:
                return False
            if valor < actual.valor:
                if actual.izquierda is None:
                    actual.izquierda = Nodo(valor)
                    return True
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    actual.derecha = Nodo(valor)
                    return True
                actual = actual.derecha

    def buscar(self, valor):
        actual = self.raiz
        while actual:
            if valor == actual.valor:
                return True
            actual = actual.izquierda if valor < actual.valor else actual.derecha
        return False

    def eliminar(self, valor):
        if not self.buscar(valor):
            return False
        self.raiz = self._eliminar(self.raiz, valor)
        return True

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            if nodo.derecha is None:
                return nodo.izquierda
            sucesor = nodo.derecha
            while sucesor.izquierda:
                sucesor = sucesor.izquierda
            nodo.valor = sucesor.valor
            nodo.derecha = self._eliminar(nodo.derecha, sucesor.valor)
        return nodo

    def recorrer(self, modo):
        resultado = []
        def visitar(nodo):
            if nodo is None:
                return
            if modo == 'preorden':
                resultado.append(nodo.valor)
            visitar(nodo.izquierda)
            if modo == 'inorden':
                resultado.append(nodo.valor)
            visitar(nodo.derecha)
            if modo == 'postorden':
                resultado.append(nodo.valor)
        visitar(self.raiz)
        return resultado

    def cantidad(self):
        return len(self.recorrer('inorden'))

    def altura(self):
        def calcular(nodo):
            return 0 if nodo is None else 1 + max(calcular(nodo.izquierda), calcular(nodo.derecha))
        return calcular(self.raiz)


class Aplicacion:
    FONDO = '#101827'
    PANEL = '#1b293d'
    TEXTO = '#edf5ff'
    ACENTO = '#21c7d9'

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title('Laboratorio de árboles binarios | Python')
        self.ventana.geometry('1100x720')
        self.ventana.minsize(780, 560)
        self.ventana.configure(bg=self.FONDO)
        self.arbol = Arbol()
        self.destacado = None
        self.animacion = []
        self.paso = 0
        self.after_id = None

        cabecera = tk.Frame(ventana, bg=self.FONDO)
        cabecera.pack(fill='x', padx=22, pady=(17, 8))
        tk.Label(cabecera, text='LABORATORIO DE ÁRBOLES BINARIOS', font=('Segoe UI', 19, 'bold'),
                 fg=self.TEXTO, bg=self.FONDO).pack(anchor='w')
        tk.Label(cabecera, text='Inserta, busca, elimina y descubre los recorridos de un árbol binario de búsqueda',
                 font=('Segoe UI', 10), fg='#a6bed6', bg=self.FONDO).pack(anchor='w')

        controles = tk.Frame(ventana, bg=self.PANEL, padx=14, pady=12)
        controles.pack(fill='x', padx=22, pady=8)
        tk.Label(controles, text='Valor:', fg=self.TEXTO, bg=self.PANEL,
                 font=('Segoe UI', 11)).pack(side='left', padx=(0, 6))
        self.entrada = tk.Entry(controles, width=9, font=('Segoe UI', 12), justify='center')
        self.entrada.pack(side='left', padx=(0, 10))
        self.entrada.bind('<Return>', lambda _e: self.insertar())
        for texto, comando in [('Insertar', self.insertar), ('Buscar', self.buscar),
                                ('Eliminar', self.eliminar), ('Ejemplo', self.ejemplo),
                                ('Limpiar', self.limpiar)]:
            tk.Button(controles, text=texto, command=comando, bg=self.ACENTO,
                      fg='#10202b', activebackground='#80e9f0', relief='flat',
                      font=('Segoe UI', 10, 'bold'), padx=9, pady=7).pack(side='left', padx=3)

        recorrido = tk.Frame(ventana, bg=self.FONDO)
        recorrido.pack(fill='x', padx=22, pady=7)
        tk.Label(recorrido, text='RECORRIDOS:', bg=self.FONDO, fg=self.TEXTO,
                 font=('Segoe UI', 10, 'bold')).pack(side='left', padx=(0, 10))
        for modo in ['preorden', 'inorden', 'postorden']:
            tk.Button(recorrido, text=modo.capitalize(), command=lambda m=modo: self.recorrer(m),
                      bg='#314660', fg='white', activebackground='#4c6789',
                      relief='flat', padx=15, pady=7).pack(side='left', padx=4)

        self.canvas = tk.Canvas(ventana, bg='#152237', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True, padx=22, pady=(5, 8))
        self.canvas.bind('<Configure>', lambda _e: self.dibujar())

        pie = tk.Frame(ventana, bg=self.FONDO)
        pie.pack(fill='x', padx=22, pady=(0, 16))
        self.estado = tk.Label(pie, text='Selecciona «Ejemplo» para comenzar.', bg=self.FONDO,
                               fg=self.ACENTO, anchor='w', font=('Segoe UI', 11))
        self.estado.pack(fill='x')
        self.info = tk.Label(pie, text='', bg=self.FONDO, fg='#a6bed6', anchor='w',
                             font=('Segoe UI', 10))
        self.info.pack(fill='x', pady=(5, 0))
        self.dibujar()

    def valor(self):
        try:
            return int(self.entrada.get().strip())
        except ValueError:
            messagebox.showwarning('Dato inválido', 'Escribe un número entero válido.')
            return None

    def detener(self):
        if self.after_id is not None:
            self.ventana.after_cancel(self.after_id)
            self.after_id = None
        self.animacion = []
        self.destacado = None

    def insertar(self):
        numero = self.valor()
        if numero is None:
            return
        self.detener()
        if self.arbol.insertar(numero):
            self.destacado = numero
            self.estado.config(text=f'✓ Nodo {numero} insertado correctamente.')
        else:
            self.estado.config(text=f'⚠ El número {numero} ya existe; no se permiten duplicados.')
        self.dibujar()

    def buscar(self):
        numero = self.valor()
        if numero is None:
            return
        self.detener()
        existe = self.arbol.buscar(numero)
        self.destacado = numero if existe else None
        self.estado.config(text=f'✓ Encontramos el nodo {numero}.' if existe else f'✗ El nodo {numero} no existe.')
        self.dibujar()

    def eliminar(self):
        numero = self.valor()
        if numero is None:
            return
        self.detener()
        existe = self.arbol.eliminar(numero)
        self.estado.config(text=f'✓ Nodo {numero} eliminado.' if existe else f'✗ No se puede eliminar: {numero} no existe.')
        self.dibujar()

    def ejemplo(self):
        self.detener()
        self.arbol = Arbol()
        for numero in [50, 30, 70, 20, 40, 60, 80]:
            self.arbol.insertar(numero)
        self.estado.config(text='✓ Ejemplo creado: 50, 30, 70, 20, 40, 60, 80.')
        self.dibujar()

    def limpiar(self):
        self.detener()
        self.arbol = Arbol()
        self.estado.config(text='Árbol vacío. Inserta un número para comenzar.')
        self.dibujar()

    def recorrer(self, modo):
        self.detener()
        self.animacion = self.arbol.recorrer(modo)
        if not self.animacion:
            self.estado.config(text='El árbol está vacío. Agrega nodos primero.')
            return
        self.paso = 0
        self.avanzar(modo)

    def avanzar(self, modo):
        if self.paso >= len(self.animacion):
            self.after_id = None
            self.destacado = None
            self.estado.config(text=f'{modo.capitalize()}: ' + ' → '.join(map(str, self.animacion)))
            self.dibujar()
            return
        self.destacado = self.animacion[self.paso]
        self.estado.config(text=f'{modo.capitalize()} · Paso {self.paso + 1}/{len(self.animacion)} · Nodo {self.destacado}')
        self.dibujar()
        self.paso += 1
        self.after_id = self.ventana.after(550, lambda: self.avanzar(modo))

    def dibujar(self):
        self.canvas.delete('all')
        ancho = max(self.canvas.winfo_width(), 700)
        alto = max(self.canvas.winfo_height(), 300)
        if self.arbol.raiz is None:
            self.canvas.create_text(ancho / 2, alto / 2, text='Tu árbol aparecerá aquí 🌳',
                                    fill='#a6bed6', font=('Segoe UI', 18, 'bold'))
        else:
            niveles = max(self.arbol.altura(), 1)
            separacion_y = min(90, max(48, (alto - 95) / max(niveles, 1)))
            radio = 20 if niveles > 6 else 23

            def pintar(nodo, x, y, espacio):
                if nodo is None:
                    return
                hijos = [(nodo.izquierda, x - espacio), (nodo.derecha, x + espacio)]
                for hijo, hx in hijos:
                    if hijo:
                        self.canvas.create_line(x, y, hx, y + separacion_y,
                                                fill='#64819f', width=2)
                        pintar(hijo, hx, y + separacion_y, max(18, espacio / 2))
                marcado = nodo.valor == self.destacado
                self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio,
                                        fill='#18c9a6' if marcado else '#273f5d',
                                        outline='#8ff7e0' if marcado else '#21c7d9', width=2)
                self.canvas.create_text(x, y, text=str(nodo.valor), fill='white',
                                        font=('Segoe UI', 12, 'bold'))

            pintar(self.arbol.raiz, ancho / 2, 48, ancho / 4)
        raiz = self.arbol.raiz.valor if self.arbol.raiz else '—'
        self.info.config(text=f'Nodos: {self.arbol.cantidad()}     |     Altura: {self.arbol.altura()}     |     Raíz: {raiz}')


if __name__ == '__main__':
    raiz = tk.Tk()
    Aplicacion(raiz)
    raiz.mainloop()

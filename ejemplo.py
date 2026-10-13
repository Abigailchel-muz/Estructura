import tkinter as tk
from tkinter import messagebox

class PilaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Pila (Stack) - Modo Gráfico")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")
        
        self.pila = []
        self.capacidad_max = 8 # Límite visual para la interfaz

        # Título
        titulo = tk.Label(root, text="Estructura de Datos: Pila (LIFO)", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333")
        titulo.pack(pady=15)

        # Marco para la entrada de datos
        frame_input = tk.Frame(root, bg="#f0f0f0")
        frame_input.pack(pady=5)

        self.entry_dato = tk.Entry(frame_input, font=("Arial", 12), width=15)
        self.entry_dato.pack(side=tk.LEFT, padx=5)
        self.entry_dato.bind("<Return>", lambda event: self.push()) # Permitir Enter

        btn_push = tk.Button(frame_input, text="Apilar (Push)", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=self.push)
        btn_push.pack(side=tk.LEFT, padx=5)

        # Marco para acciones de la Pila
        frame_acciones = tk.Frame(root, bg="#f0f0f0")
        frame_acciones.pack(pady=10)

        btn_pop = tk.Button(frame_acciones, text="Desapilar (Pop)", font=("Arial", 10, "bold"), bg="#F44336", fg="white", command=self.pop)
        btn_pop.pack(side=tk.LEFT, padx=5)

        btn_peek = tk.Button(frame_acciones, text="Ver Cima (Peek)", font=("Arial", 10, "bold"), bg="#FF9800", fg="white", command=self.peek)
        btn_peek.pack(side=tk.LEFT, padx=5)

        btn_limpiar = tk.Button(frame_acciones, text="Limpiar", font=("Arial", 10, "bold"), bg="#607D8B", fg="white", command=self.limpiar)
        btn_limpiar.pack(side=tk.LEFT, padx=5)

        # Lienzo / Contenedor visual de la Pila
        lbl_visual_titulo = tk.Label(root, text="Representación gráfica de la Pila:", font=("Arial", 10, "italic"), bg="#f0f0f0", fg="#666")
        lbl_visual_titulo.pack(pady=(10, 0))

        self.frame_canvas = tk.Frame(root, bg="white", bd=2, relief=tk.SUNKEN, width=220, height=260)
        self.frame_canvas.pack(pady=10)
        self.frame_canvas.pack_propagate(False)

        # Etiquetas visuales que simulan los bloques de la pila (desde la base hasta la cima)
        self.cajas_pila = []
        for _ in range(self.capacidad_max):
            lbl = tk.Label(self.frame_canvas, text="", font=("Arial", 11, "bold"), bg="#e0e0e0", fg="#333", width=20, height=1, relief=tk.OUTLINE if hasattr(tk, 'OUTLINE') else tk.RAISED)
            self.cajas_pila.append(lbl)
        
        # Empaquetar las cajas en orden inverso para que crezcan de abajo hacia arriba
        for lbl in reversed(self.cajas_pila):
            lbl.pack(pady=2)

        self.actualizar_visualizacion()

    def push(self):
        dato = self.entry_dato.get().strip()
        if not dato:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un valor.")
            return
        
        if len(self.pila) >= self.capacidad_max:
            messagebox.showerror("Desbordamiento (Overflow)", "La pila está llena.")
            return

        self.pila.append(dato)
        self.entry_dato.delete(0, tk.END)
        self.actualizar_visualizacion()

    def pop(self):
        if not self.pila:
            messagebox.showerror("Subdesbordamiento (Underflow)", "La pila está vacía.")
            return
        
        eliminado = self.pila.pop()
        messagebox.showinfo("Elemento Removido", f"Se ha desapilado el elemento: '{eliminado}'")
        self.actualizar_visualizacion()

    def peek(self):
        if not self.pila:
            messagebox.showinfo("Cima de la Pila", "La pila está vacía.")
            return
        
        cima = self.pila[-1]
        messagebox.showinfo("Cima de la Pila", f"El elemento en la cima es: '{cima}'")

    def limpiar(self):
        self.pila.clear()
        self.actualizar_visualizacion()

    def actualizar_visualizacion(self):
        # Limpiar todas las cajas visuales
        for lbl in self.cajas_pila:
            lbl.config(text="", bg="#e0e0e0")

        # Rellenar desde la base con los elementos actuales de la pila
        # En una pila LIFO, el último elemento añadido está en la cima visual superior de los elementos activos
        total_elementos = len(self.pila)
        for i in range(total_elementos):
            # Mapeamos desde el fondo del canvas
            idx_caja = self.capacidad_max - total_elementos + i
            elemento = self.pila[i]
            
            # Destacar la cima con un color diferente
            if i == total_elementos - 1:
                self.cajas_pila[idx_caja].config(text=f"CIMA -> {elemento}", bg="#4CAF50", fg="white")
            else:
                self.cajas_pila[idx_caja].config(text=elemento, bg="#90CAF9", fg="#000")

if __name__ == "__main__":
    root = tk.Tk()
    app = PilaGUI(root)
    root.mainloop()
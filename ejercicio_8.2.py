import tkinter as tk
from tkinter import ttk

class VentanaPrincipal(tk.Tk):
    """
    Clase que crea una interfaz gráfica básica utilizando Tkinter.
    Versión 1.0 / 2026
    """
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 8.2 - Componentes Tkinter")
        self.geometry("300x200")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        """Método que inicializa y ubica los componentes en la ventana"""

        self.label_nombre = ttk.Label(self, text="Nombre:")
        self.campo_nombre = ttk.Entry(self)
        
        self.label_edad = ttk.Label(self, text="Edad:")
        self.campo_edad = ttk.Entry(self)
        
        self.boton_aceptar = ttk.Button(self, text="Aceptar")


        self.label_nombre.grid(row=0, column=0, padx=15, pady=15, sticky="w")
        self.campo_nombre.grid(row=0, column=1, padx=15, pady=15)
        
        self.label_edad.grid(row=1, column=0, padx=15, pady=5, sticky="w")
        self.campo_edad.grid(row=1, column=1, padx=15, pady=5)
        
        self.boton_aceptar.grid(row=2, column=0, columnspan=2, pady=15)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
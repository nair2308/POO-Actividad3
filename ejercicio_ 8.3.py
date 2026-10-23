import tkinter as tk
from tkinter import ttk

class VentanaEventos(tk.Tk):
    """
    Clase que gestiona eventos de interacción de usuario en Tkinter.
    Versión 1.0 / 2026
    """
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 8.3 - Gestión de Eventos")
        self.geometry("350x220")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        """Método que inicializa los componentes y registra el evento del botón"""

        self.label_dato = ttk.Label(self, text="Ingrese un valor:")
        self.campo_dato = ttk.Entry(self, width=22)
        

        self.boton_procesar = ttk.Button(self, text="Procesar", command=self.procesar_evento)
        
        self.label_resultado = ttk.Label(self, text="Resultado: ", font=("Arial", 10, "bold"))

        self.label_dato.pack(pady=(20, 5))
        self.campo_dato.pack(pady=5)
        self.boton_procesar.pack(pady=10)
        self.label_resultado.pack(pady=10)

    def procesar_evento(self):
        """Método que captura y gestiona la acción (Click del botón)"""
        texto = self.campo_dato.get()
        if texto.strip() != "":
            self.label_resultado.config(text=f"Resultado: Hola, {texto}")
        else:
            self.label_resultado.config(text="Resultado: ¡Por favor ingresa un valor!")

if __name__ == "__main__":
    app = VentanaEventos()
    app.mainloop()
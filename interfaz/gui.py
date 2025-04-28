import tkinter as tk
from main import Juego

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Ejército")
        self.geometry("400x300")

        label = tk.Label(self, text="Bienvenido al Gestor de Ejército", font=("Arial", 14))
        label.pack(pady=20)

        btn = tk.Button(self, text="Iniciar Cálculo", command=self.iniciar)
        btn.pack(pady=10)

    def iniciar(self):
        Juego.mostrar_recursos()

if __name__ == "__main__":
    app = App()
    app.mainloop()

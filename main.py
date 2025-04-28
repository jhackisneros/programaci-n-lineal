import tkinter as tk
from recursos.comida import Comida
from recursos.madera import Madera
from recursos.oro import Oro

class Juego:
    @staticmethod
    def mostrar_recursos():
        try:
            comida = Comida.obtener_comida()
            madera = Madera.obtener_madera()
            oro = Oro.obtener_oro()

            if comida is None or madera is None or oro is None:
                raise ValueError("Uno o más recursos no se pudieron obtener correctamente.")

            return f"Recursos disponibles:\n - 🍗 Comida: {comida}\n - 🪵 Madera: {madera}\n - 🪙 Oro: {oro}"
        except AttributeError as e:
            return f"Error al obtener recursos: {e}"
        except ValueError as e:
            return f"Error en los valores de los recursos: {e}"
        except Exception as e:
            return f"Ha ocurrido un error inesperado: {e}"

# Crear la ventana GUI
def mostrar_en_gui():
    recursos = Juego.mostrar_recursos()
    label_resultado.config(text=recursos)

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Recursos del Juego")

    label_titulo = tk.Label(ventana, text="Recursos del Juego", font=("Arial", 16))
    label_titulo.pack(pady=10)

    boton_mostrar = tk.Button(ventana, text="Mostrar Recursos", command=mostrar_en_gui)
    boton_mostrar.pack(pady=10)

    label_resultado = tk.Label(ventana, text="", font=("Arial", 12), justify="left")
    label_resultado.pack(pady=10)

    ventana.mainloop()
from unidades.espadachin import Espadachin
from unidades.arquero import Arquero
from unidades.jinete import Jinete
from recursos.comida import Comida
from recursos.madera import Madera
from recursos.oro import Oro

class Juego:
    @staticmethod
    def mostrar_recursos():
        comida = Comida.obtener_comida()
        madera = Madera.obtener_madera()
        oro = Oro.obtener_oro()

        print(f"Recursos disponibles: \nComida: {comida}, Madera: {madera}, Oro: {oro}")

if __name__ == "__main__":
    Juego.mostrar_recursos()

from recursos.comida import Comida
from recursos.madera import Madera
from recursos.oro import Oro
from unidades.espadachin import Espadachin
from unidades.arquero import Arquero
from unidades.jinete import Jinete

class OptimizadorEjercito:
    def __init__(self, comida, madera, oro):
        self.comida = comida
        self.madera = madera
        self.oro = oro

        # Definir las unidades disponibles
        self.swordsmen = Espadachin('Espadachín', 50, 30, 0)
        self.bowmen = Arquero('Arquero', 40, 20, 40)
        self.horsemen = Jinete('Jinete', 60, 40, 100)

    def calcular_unidades_optimas(self):
        # Definimos los costes por unidad
        comida_swordsmen = 60
        madera_swordsmen = 20
        oro_swordsmen = 0

        comida_bowmen = 80
        madera_bowmen = 10
        oro_bowmen = 40

        comida_horsemen = 140
        madera_horsemen = 40
        oro_horsemen = 100

        # Inicializamos el mejor conjunto de unidades
        mejor_composicion = {
            'espadachines': 0,
            'arqueros': 0,
            'jinetes': 0,
            'poder_total': 0
        }

        for espadachines in range(self.comida // comida_swordsmen + 1):
            for arqueros in range(self.comida // comida_bowmen + 1):
                for jinetes in range(self.comida // comida_horsemen + 1):
                    # Calcular recursos requeridos
                    comida_total = espadachines * comida_swordsmen + arqueros * comida_bowmen + jinetes * comida_horsemen
                    madera_total = espadachines * madera_swordsmen + arqueros * madera_bowmen + jinetes * madera_horsemen
                    oro_total = espadachines * oro_swordsmen + arqueros * oro_bowmen + jinetes * oro_horsemen

                    # Verificamos si los recursos no exceden los disponibles
                    if comida_total <= self.comida and madera_total <= self.madera and oro_total <= self.oro:
                        poder_total = (espadachines * self.swordsmen.poder() + 
                                       arqueros * self.bowmen.poder() + 
                                       jinetes * self.horsemen.poder())

                        # Actualizamos la mejor composición si es una mejor solución
                        if poder_total > mejor_composicion['poder_total']:
                            mejor_composicion = {
                                'espadachines': espadachines,
                                'arqueros': arqueros,
                                'jinetes': jinetes,
                                'poder_total': poder_total
                            }

        return mejor_composicion

if __name__ == "__main__":
    # Ejemplo de recursos disponibles
    comida = Comida.obtener_comida()
    madera = Madera.obtener_madera()
    oro = Oro.obtener_oro()

    optimizador = OptimizadorEjercito(comida, madera, oro)
    mejor_composicion = optimizador.calcular_unidades_optimas()

    print("================= Solución Óptima =================")
    print(f"Poder total = {mejor_composicion['poder_total']} 💪")
    print(f"Composición del ejército:")
    print(f" - 🗡️ Espadachines = {mejor_composicion['espadachines']}")
    print(f" - 🏹 Arqueros = {mejor_composicion['arqueros']}")
    print(f" - 🐎 Jinetes = {mejor_composicion['jinetes']}")

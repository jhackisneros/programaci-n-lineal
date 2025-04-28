# unidades/espadachines.py

class Espadachin:
    def __init__(self, nombre, ataque, defensa, coste_oro):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.coste_oro = coste_oro

    def poder(self):
        """Calcula el poder total del espadachín"""
        return self.ataque * 2 + self.defensa

class Arquero:
    def __init__(self, nombre, ataque, defensa, coste_oro):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.coste_oro = coste_oro

    def poder(self):
        return self.ataque * 1.8 + self.defensa

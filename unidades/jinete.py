class Jinete:
    def __init__(self, nombre, ataque, defensa, coste_oro):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.coste_oro = coste_oro

    def poder(self):
        return self.ataque * 2.5 + self.defensa * 1.5

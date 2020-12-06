class Nodo:
    def __init__(self):
        self.dato = None
        self.derecho = None
        self.izquierdo = None
        self.peso = 0

    def getDato(self):
        return str(self.dato)

    def getPeso(self):
        return int(self.peso)
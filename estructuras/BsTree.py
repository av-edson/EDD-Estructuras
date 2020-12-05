# CLASE PARA EL NODO
class Node:
    def __init__(self, dato):
        self.dato = dato
        self.derecho = None
        self.izquierdo = None
        self.altura = None
       

class ArbolB:
    def __init__(self):
        self.raiz = None

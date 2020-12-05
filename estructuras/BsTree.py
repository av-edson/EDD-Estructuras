# CLASE PARA EL NODO
class Node:
    def __init__(self, dato):
        self.dato = dato
        self.derecho = None
        self.izquierdo = None
        self.altura = None

    """ Regresa un String para graficar el Arbol"""
    def getDato(self):
        return str(self.dato)


class ArbolB:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = self.nuevoNodo(valor)
        else:
            print('agregar')

    def nuevoNodo(self, valor):
        return Node(valor)


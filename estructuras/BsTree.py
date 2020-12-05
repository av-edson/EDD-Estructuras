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
            self.raiz.altura = 0
        else:
            self.raiz = self.recursivoAgregar(valor, self.raiz)

    def recursivoAgregar(self, valor, aux):
        temporal = Node(valor)
        temporal.altura = aux.altura + 1

        if aux.dato > valor:
            # print('es menor') SE VA A LA IZQUIERDA
            if aux.izquierdo is None:
                aux.izquierdo = temporal
                return aux
        elif aux.dato == valor:
            print('El dato ' + str(valor) + ' es repetido y no se admite')
            return aux
        else:
            # print('es mayor')
            if aux.derecho is None:
                aux.derecho = temporal
                return aux
        return None

    def nuevoNodo(self, valor):
        return Node(valor)


arbol = ArbolB()
arbol.agregar(5)
arbol.agregar(2)
arbol.agregar(6)
arbol.agregar(5)

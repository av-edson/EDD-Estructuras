import random as rd
import graficadorArboles as graf



class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.derecho = None
        self.izquierdo = None
        self.peso = 0

    def getDato(self):
        return str(self.dato)

    def getPeso(self):
        return int(self.peso)

class AvlTree:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.raiz = self.__recursiveAdd(valor, self.raiz)

    def __recursiveAdd(self, valor, arbol):
        if valor < arbol.dato:
            if arbol.izquierdo is None:
                arbol.izquierdo = Nodo(valor)
            else:
                arbol.izquierdo = self.__recursiveAdd(valor, arbol.izquierdo)
        elif valor == arbol.dato:
            print('valor repetido')
        else:
            if arbol.derecho is None:
                arbol.derecho = Nodo(valor)
            else:
                arbol.derecho = self.__recursiveAdd(valor, arbol.derecho)
        arbol.peso = self.__pesoMax(arbol) + 1
        return arbol

    def __getPesoNodo(self, nodo):
        if nodo is None:
            return -1
        else:
            return int(nodo.peso)

    def __pesoMax(self, nodo):
        if self.__getPesoNodo(nodo.derecho) > self.__getPesoNodo(nodo.izquierdo):
            return self.__getPesoNodo(nodo.derecho)
        else:
            return self.__getPesoNodo(nodo.izquierdo)




g = AvlTree();
g.agregar(50)
for i in range(15):
    g.agregar(rd.randint(0, 100))
graficador  = graf.Graficador(g, 'avl')
graficador.exportar()


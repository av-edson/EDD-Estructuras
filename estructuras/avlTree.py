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
            if abs(self.__getPesoNodo(arbol.derecho) - self.__getPesoNodo(arbol.izquierdo)) >= 2:
                arbol = self.__simpleIzquierda(arbol)
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

    def __simpleIzquierda(self,arbol):
        aux = arbol.izquierdo
        arbol.izquierdo = aux.derecho
        aux.derecho = arbol
        arbol.peso = self.__pesoMax(arbol) + 1
        aux.peso = self.__pesoMax(aux) + 1
        return aux




g = AvlTree();
g.agregar(50)

while True:
    numero = input("Ingrese Numero: ")
    try:
        g.agregar(int(numero))
    except:
        print("Error ex")
    finally:
        graficador = graf.Graficador(g, "avl")
        graficador.exportar()


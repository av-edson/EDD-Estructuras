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
                if valor > int(arbol.izquierdo.dato):
                    arbol = self.__dobleIzquierda(arbol)
                else:
                    arbol = self.__simpleIzquierda(arbol)
        elif valor == arbol.dato:
            print('valor repetido')
        else:
            if arbol.derecho is None:
                arbol.derecho = Nodo(valor)
            else:
                arbol.derecho = self.__recursiveAdd(valor, arbol.derecho)
            if abs(self.__getPesoNodo(arbol.derecho) - self.__getPesoNodo(arbol.izquierdo)) >= 2:
                if valor > int(arbol.derecho.dato):
                    arbol = self.__simpleDerecha(arbol)
                else:
                    arbol = self.__dobleDerecha(arbol)
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

    def __simpleIzquierda(self, arbol):
        aux = arbol.izquierdo
        arbol.izquierdo = aux.derecho
        aux.derecho = arbol
        arbol.peso = self.__pesoMax(arbol) + 1
        aux.peso = self.__pesoMax(aux) + 1
        return aux

    def __simpleDerecha(self, arbol):
        aux = arbol.derecho
        arbol.derecho = aux.izquierdo
        aux.izquierdo = arbol
        arbol.peso = self.__pesoMax(arbol) + 1
        aux.peso = self.__pesoMax(aux) + 1
        return aux

    def __dobleIzquierda(self, arbol):
        arbol.izquierdo = self.__simpleDerecha(arbol.izquierdo)
        return self.__simpleIzquierda(arbol)

    def __dobleDerecha(self, arbol):
        arbol.derecho = self.__simpleIzquierda(arbol.derecho)
        return self.__simpleDerecha(arbol)

    # para eliminar Nodos
    def eliminarNodo(self, valor):
        self.__eliminar(valor, self.raiz, None)

    def __eliminar(self, valor, arbol, padre):
        if arbol is None:
            print("Valor no Existente en el Arbol")
            return
        elif valor == arbol.dato:
            if padre.derecho == arbol:
                if self.__getPesoNodo(arbol) == 0:
                    padre.derecho = None
            else:
                if self.__getPesoNodo(arbol) == 0:
                    padre.izquierdo = None
        elif valor < arbol.dato:
            self.__eliminar(valor, arbol.izquierdo, arbol)
        else:
            self.__eliminar(valor, arbol.derecho, arbol)


def mostrarMenu():
    print("1 - para agregar")
    print("2 - para eliminar")
    return input("Ingrese Opcion: ")


g = AvlTree()
g.agregar(50)
while True:
    opcion = mostrarMenu()
    numero = input("Ingrese Numero: ")
    try:
        if opcion == "1":
            g.agregar(int(numero))
        elif opcion == "2":
            g.eliminarNodo(int(numero))
    except:
        print("Error ex")
    finally:
        graficador = graf.Graficador(g, "avl")
        graficador.exportar()


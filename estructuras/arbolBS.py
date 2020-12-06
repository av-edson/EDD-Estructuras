import graficadorArboles as Gr
import random


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


class ArbolBS:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
            self.raiz.altura = 0
        else:
            self.raiz = self.__recursivoAgregar(valor, self.raiz)

    def __recursivoAgregar(self, valor, aux):
        temporal = Node(valor)
        temporal.altura = aux.altura + 1

        if aux.dato > valor:
            # print('es menor') SE VA A LA IZQUIERDA
            if aux.izquierdo is None:
                aux.izquierdo = temporal
                return aux
            else:
                aux.izquierdo = self.__recursivoAgregar(valor, aux.izquierdo)
                return aux
        elif aux.dato == valor:
            print('El dato ' + str(valor) + ' es repetido y no se admite')
            return aux
        else:
            # print('es mayor')
            if aux.derecho is None:
                aux.derecho = temporal
                return aux
            else:
                aux.derecho = self.__recursivoAgregar(valor, aux.derecho)
                return aux

    def buscarElemento(self, valor, arbol):
        if arbol is None:
            return False
        elif valor < arbol.dato:
            return self.buscarElemento(valor, arbol.izquierdo)
        elif valor > arbol.dato:
            return self.buscarElemento(valor, arbol.derecho)
        else:
            return True


# graficador e ingreso terminado
arbol = ArbolBS()
arbol.agregar(50)
for i in range(20):
    if i == 10:
        arbol.agregar(15)
        continue
    elif i == 18:
        arbol.agregar(76)
        continue
    arbol.agregar(random.randint(0, 100))

graficador = Gr.Graficador(arbol, 'bs')
graficador.exportar()
print(arbol.buscarElemento(15, arbol.raiz))
print(arbol.buscarElemento(76, arbol.raiz))
print(arbol.buscarElemento(150, arbol.raiz))
print(arbol.buscarElemento(-150, arbol.raiz))
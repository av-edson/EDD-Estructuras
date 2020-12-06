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


# graficador e ingreso terminado
arbol = ArbolBS()
# agregamos numeros
arbol.agregar(100)
for i in range(200):
    arbol.agregar(random.randint(-2000, 2000))

graficador = Gr.Graficador(arbol, 'bs')
graficador.exportar()

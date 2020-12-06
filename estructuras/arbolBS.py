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

    def eliminarElemento(self, valor, arbol, padre):
        if arbol is None:
            print('El elemento a Eliminar no Existe :)')
            return False
        elif valor < arbol.dato:
            self.eliminarElemento(valor, arbol.izquierdo, arbol)
        elif valor > arbol.dato:
            self.eliminarElemento(valor, arbol.derecho, arbol)
        else:
            # es una hoja
            if arbol.izquierdo is None and arbol.derecho is None:
                # borramos relacion derecha
                if padre.derecho == arbol:
                    padre.derecho = None
                # borramos relacion izquierda
                else:
                    padre.izquierdo = None
                return True


# graficador e ingreso terminado
arbol = ArbolBS()
arbol.agregar(50)
arbol.agregar(52)
arbol.agregar(48)
arbol.agregar(55)
arbol.agregar(43)

# para graficar
graficador = Gr.Graficador(arbol, 'bs')
graficador.exportar()

arbol.eliminarElemento(43, arbol.raiz, None)
arbol.eliminarElemento(55, arbol.raiz, None)

graficador = Gr.Graficador(arbol, 'bs')
graficador.exportar()

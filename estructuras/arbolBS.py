import graficadorArboles as Gr


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
            if arbol.izquierdo is None and arbol.derecho is None and padre is not None:
                # borramos relacion derecha
                if padre.derecho == arbol:
                    padre.derecho = None
                # borramos relacion izquierda
                else:
                    padre.izquierdo = None
            # tiene un hijo derecho
            elif arbol.derecho is not None and arbol.izquierdo is None and padre is not None:
                if padre.derecho == arbol:
                    padre.derecho = arbol.derecho
                else:
                    padre.izquierdo = arbol.derecho
            # tiene un hijo izquierdo
            elif arbol.izquierdo is not None and arbol.derecho is None and padre is not None:
                if padre.izquierdo == arbol:
                    padre.izquierdo = arbol.izquierdo
                else:
                    padre.derecho = arbol.izquierdo
            # tiene dos hijos
            else:
                # si es raiz
                if padre is None:
                    aux = self.getNodoEliminar(arbol.derecho, arbol)
                    arbol.dato = aux
                elif padre.izquierdo == arbol:
                    # solo hay que remplazar el valor
                    aux = self.getNodoEliminar(arbol.derecho, arbol)
                    padre.izquierdo.dato = aux
                else:
                    padre.derecho = self.getNodoEliminar(arbol.derecho, arbol)
            return True

    def getNodoEliminar(self, nodo, padre):
        if nodo.izquierdo is None:
            padre.izquierdo = None
            return nodo.getDato()
        else:
            return self.getNodoEliminar(nodo.izquierdo, nodo)


# graficador e ingreso terminado
arbol = ArbolBS()
arbol.agregar(55)
arbol.agregar(50)
arbol.agregar(48)
arbol.agregar(53)
arbol.agregar(51)
arbol.agregar(49)
arbol.agregar(40)
arbol.agregar(54)

# para graficar
graficador = Gr.Graficador(arbol, 'bs')
graficador.exportar()

arbol.eliminarElemento(55, arbol.raiz, None)

graficador = Gr.Graficador(arbol, 'bs')
graficador.exportar()

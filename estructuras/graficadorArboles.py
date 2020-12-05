import os


class Graficador:
    def __init__(self, arbol, tipo):
        self.contenido = ""
        self.arbol = arbol
        if tipo == 'bs':
            self.titulo = 'Arbol Binario De Busqueda BS'
        elif tipo == 'avl':
            self.titulo = 'Arbol Binario Balanceado AVL'

    def graficar(self):
        self.contenido = str(self.arbol.dato) + "\n"
        self.contenidoRecursivo(self.arbol)

    def contenidoRecursivo(self, aux):
        if aux.derecho is not None:
            self.contenido = self.contenido + aux.dato + " -> " + aux.derecho.dato + "\n"
            self.contenidoRecursivo(aux.derecho)
        elif aux.izquierdo is not None:
            self.contenido = self.contenido + aux.dato + " -> " + aux.izquierdo.dato + "\n"
            self.contenidoRecursivo(aux.izquierdo)
        else:
            return

    def exportar(self):
        archivo = open('GraficaArbol.dot', 'w')
        archivo.write('digraph D{\n')
        archivo.write("rankdir=LR; \n")
        archivo.write("node [shape=circle style=filled ] \n")
        archivo.write("label=  Grafico del " + self.titulo + " \n")

        # se agrega el contenido al dot
        archivo.write(self.contenido)

        # cerramos el archivo . dot y el de python
        archivo.write('\n}')
        archivo.close()

        # exportamos
        os.system('dot -Tpdf DocomentoDot.dot -o Grafico.pdf')

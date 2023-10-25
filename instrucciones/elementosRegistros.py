from abstract.abstract import Expression

class ElementosRegistros(Expression):

    def __init__(self, elementos, fila, columna):
        self.elementos = elementos
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):
        return self.elementos

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
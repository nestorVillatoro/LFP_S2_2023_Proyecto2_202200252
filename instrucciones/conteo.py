from abstract.abstract import Expression

class Conteo(Expression):

        def __init__(self, contador, fila, columna):
            self.contador = contador
            super().__init__(fila, columna)

        def operar(self, arbol):
            pass

        def ejecutarT(self):
            return self.contador

        def getFila(self):
            return super().getFila()

        def getColumna(self):
            return super().getColumna()
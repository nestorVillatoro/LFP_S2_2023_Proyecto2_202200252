from abstract.abstract import Expression

class Datos(Expression):

        def __init__(self, verificador, fila, columna):
            self.verificador = verificador
            super().__init__(fila, columna)

        def operar(self, arbol):
            pass

        def ejecutarT(self):
            return self.verificador

        def getFila(self):
            return super().getFila()

        def getColumna(self):
            return super().getColumna()
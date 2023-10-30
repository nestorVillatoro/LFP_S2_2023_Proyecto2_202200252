from abstract.abstract import Expression

class Numero(Expression):

    def __init__(self, lexema, fila, columna, tipo):
        self.lexema = lexema
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        return self.lexema

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
from abstract.abstract import Expression

class Contarsi(Expression):

        def __init__(self, texto, numero, fila, columna):
            self.texto = texto
            self.numero = numero
            super().__init__(fila, columna)

        def operar(self, arbol):
            pass

        def ejecutarT(self):
            return self.texto
        
        def ejecutarN(self):
            return self.numero

        def getFila(self):
            return super().getFila()

        def getColumna(self):
            return super().getColumna()
from abstract.abstract import Expression

class DeclaracionRegistros(Expression):

    def __init__(self, cant, nombre, elementos, fila, columna):
        self.nombre = nombre
        self.cant = cant
        self.elementos = elementos
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):
        return self.elementos
    
    def obtenerCant(self):
        return self.cant

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()

class Celular:
    """
    Dispositivo para diversas aplicaciones.
    La forma de calcular el precio cambia por las características del celular, 
    pero no se desea que el programa quede con condicionales complejos o con
    una jerarquía de herencia muy extensa.
    """
    def __init__(self, modelo, memoria):
        self.modelo = modelo
        self.memoria = memoria
    
    def calcular_precio(self):
        """
        El precio depende de varios factores. Las caractetísticas extra pueden cambiarlo.
        """
        precio = 500000
        precio+= self.memoria * 1200
        return precio

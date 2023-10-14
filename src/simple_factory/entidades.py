from abc import ABC, abstractmethod

class Juguete(ABC):
    """
    Juguete que puede ser de diferentes tipos.
    CORRESPONDE AL ROL "PRODUCT" del Simple Factory.
    """
    
    def __init__(self, nombre, precio_base, volumen):
        self.nombre = nombre
        self.precio_base = precio_base
        self.volumen = volumen
    
    @abstractmethod
    def get_precio_total(self) -> float:
        """
        Calcula el precio total del juguete, con cargos e impuestos.
        """


class Muneco(Juguete):
    """
    Figura de animales, personajes de acción o personas, para jugar.
    CORRESPONDE AL ROL "CONCRETE PRODUCT" del Simple Factory.
    """

    def get_precio_total(self):
        return self.precio_base + self.volumen*100


class Balon(Juguete):
    """
    Balón de colores y exterior suave.
    CORRESPONDE AL ROL "CONCRETE PRODUCT" del Simple Factory.
    """

    def get_precio_total(self):
        return self.precio_base + self.volumen*50


class Tren(Juguete):
    """
    Tren de juguete de madera.
    CORRESPONDE AL ROL "CONCRETE PRODUCT" del Simple Factory.
    """

    def get_precio_total(self):
        return self.precio_base*2 + self.volumen*100

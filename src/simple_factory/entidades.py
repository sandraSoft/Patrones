""" 
Jerarquía de clases usada en un juguetería
Version: 1.0
"""

from abc import ABC, abstractmethod

class Juguete(ABC):
    """
    Juguete para bebé, con hijas para los diferentes juguetes que se deseen
    """
    
    def __init__(self, precio_base, volumen):
        self.precio_base = precio_base
        self.volumen = volumen
    
    @abstractmethod
    def get_precio_total(self):
        """
        Calcula el precio total del juguete, incluyendo el precio del empaque
        """
        pass


class Peluche(Juguete):
    """
    Juguete de peluche para bebé
    """

    def get_precio_total(self):
        return self.precio_base + self.volumen*100


class Balon(Juguete):
    """
    Balón de colores para bebé
    """

    def get_precio_total(self):
        return self.precio_base + self.volumen*50
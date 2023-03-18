from abc import ABC, abstractmethod

class Celular(ABC):
    """
    Dispositivo para diversas aplicaciones.
    La forma de calcular el precio cambia por las características del celular, 
    para lo cual se usará el patrón DECORATOR (esta clase corresponde al "Component").
    """
    @abstractmethod
    def calcular_precio(self):
        """
        El precio depende de varios factores. Las caractetísticas extra pueden cambiarlo.
        """


class CelularBase(Celular):
    """
    Corresponde al celular base (que era el que estaba originalmente),
    al cual se le pueden adicionar características extra.
    Se usa el patrón DECORATOR (esta clase corresponde al "Concrete Component").
    """
    def __init__(self, modelo, memoria):
        self.modelo = modelo
        self.memoria = memoria
    
    def calcular_precio(self):
        precio = 500000
        precio+= self.memoria * 1200
        return precio


class Adicional(Celular):
    """
    Permite extender las características de un celular base.
    Corresponde al patrón DECORATOR (rol "Decorator").
    """
    def __init__(self, celular):
        self.celular = celular
    
    def calcular_precio(self):
        return self.celular.calcular_precio()


class Usado(Adicional):
    """
    Un tipo de adición o característica de un celular.
    Cambia la forma de calcular el valor, a partir del precio base.
    Es un "Concrete Decorador" (patrón DECORATOR).
    """
    def calcular_precio(self):
        return super().calcular_precio() * 0.5


class ConCamara(Adicional):
    """
    Un tipo de adición o característica de un celular.
    Cambia la forma de calcular el valor, a partir del precio base.
    Es un "Concrete Decorador" (patrón DECORATOR).
    """
    def calcular_precio(self):
        return super().calcular_precio() * 1.2

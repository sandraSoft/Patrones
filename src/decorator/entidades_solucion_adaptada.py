class Celular():
    """
    Corresponde al celular base (que era el que estaba originalmente),
    al cual se le pueden adicionar características extra.
    Se usa el patrón DECORATOR -adaptado
    (esta clase corresponde tanto al "Component" como al "Concrete Component").
    """
    def __init__(self, modelo, memoria):
        self.modelo = modelo
        self.memoria = memoria
    
    def calcular_precio(self):
        precio = 500000
        precio+= self.memoria * 1200
        return precio


class CelularAdicion(Celular):
    """
    Permite extender las características de un celular base.
    Corresponde al patrón DECORATOR (rol "Decorator").
    """
    def __init__(self, base):
        self.base = base
    
    def calcular_precio(self):
        return self.base.calcular_precio()


class CelularUsado(CelularAdicion):
    """
    Un tipo de adición o característica de un celular.
    Cambia la forma de calcular el valor, a partir del precio base.
    Es un "Concrete Decorador" (patrón DECORATOR).
    """
    def calcular_precio(self):
        return super().calcular_precio() * 0.5


class CelularCamara(CelularAdicion):
    """
    Un tipo de adición o característica de un celular.
    Cambia la forma de calcular el valor, a partir del precio base.
    Es un "Concrete Decorador" (patrón DECORATOR).
    """
    def calcular_precio(self):
        return super().calcular_precio() * 1.2

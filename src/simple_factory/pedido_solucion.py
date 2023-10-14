from simple_factory.entidades import Muneco
from simple_factory.entidades import Balon
from simple_factory.entidades import Tren

class FabricaJuguetes:
    """
    CORRESPONDE AL ROL "FACTORY" del Simple Factory.
    """
    @staticmethod
    def crear_juguete(nombre, precio_base, volumen, tipo):
        if tipo == 'm':
            return Muneco(nombre, precio_base, volumen)
        elif tipo == 'b':
            return Balon(nombre, precio_base, volumen)
        elif tipo == 't':
            return Tren(nombre, precio_base, volumen)
        else:
            raise ValueError("Tipo de juguete no soportado")


class Pedido:
    """ 
    Guarda los datos de un pedido de juguetes,
    especialmente el precio, necesario para el área de Mercadeo.

    ESTA CLASE NO TIENE QUE CONOCER LAS CLASES HIJAS DE JUGUETE,
    CUMPLIENDO ASÍ CON VARIOS PRINCIPIOS DE DISEÑO.
    """
    
    def __init__(self):
        self.juguetes = []

    def adicionar_juguete(self, nombre, precio_base, volumen, tipo):
        for juguete in self.juguetes:
            if juguete.nombre == nombre:
               raise ValueError("Juguete con nombre repetido") 

        juguete = FabricaJuguetes.crear_juguete(nombre, precio_base, volumen, tipo)
        self.juguetes.append(juguete)
    
    def calcular_precio(self):
        """ 
        Calcula el precio del pedido, sumando el precio de los juguetes
        y unos gastos administrativos
        """
        GASTOS_ADMINISTRATIVOS = 2000
        precio_juguetes = 0
        for juguete in self.juguetes:
            precio_juguetes += juguete.get_precio_total()
        return precio_juguetes + GASTOS_ADMINISTRATIVOS

from simple_factory.entidades import Peluche
from simple_factory.entidades import Balon

class FabricaJuguetes:
    """
    CORRESPONDE AL ROL "FACTORY" del Simple Factory.
    """
    @staticmethod
    def crear_juguete(precio_base, volumen, tipo):
        if tipo == 'p':
            return Peluche(precio_base,volumen)
        elif tipo == 'b':
            return Balon(precio_base,volumen)
        else:
            raise ValueError("Invalid animal type")


class Pedido:
    """ 
    Permite obtener los datos de un pedido de un juguete, especialmente el precio.
 
    ESTA CLASE USA UNA FÁBRICA, ASÍ NO TIENE QUE CONOCER LAS HIJAS DE JUGUETE,
    CUMPLIENDO CON "DEPENDENCY INVERSION".
    """

    def adicionar_juguete(self, precio_base, volumen, tipo):
        self.juguete = FabricaJuguetes.crear_juguete(precio_base, volumen, tipo)
    
    def calcular_precio(self):
        """ 
        Calcula el precio del pedido, sumando el precio del juguete y los gastos administrativos
        """
        GASTOS_ADMINISTRATIVOS = 2000
        return self.juguete.get_precio_total() + GASTOS_ADMINISTRATIVOS

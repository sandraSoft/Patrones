from simple_factory.entidades import Peluche
from simple_factory.entidades import Balon

class Pedido:
    """ 
    Permite obtener los datos de un pedido de un juguete, especialmente el precio
 
    ESTA CLASE DEBE CONOCER LAS CLASES HIJAS DE JUGUETE,
    CREANDO ALTO ACOMPLAMIENTO
 
    @version 1.0
    """

    def adicionar_juguete(self, precio_base, volumen, tipo):
        if tipo == 'p':
            self.juguete = Peluche(precio_base,volumen)
        elif tipo == 'b':
            self.juguete = Balon(precio_base,volumen)
        else:
            raise ValueError("Invalid animal type")
    
    def calcular_precio(self):
        """ 
        Calcula el precio del pedido, sumando el precio del juguete y los gastos administrativos
        """
        GASTOS_ADMINISTRATIVOS = 2000
        return self.juguete.get_precio_total() + GASTOS_ADMINISTRATIVOS

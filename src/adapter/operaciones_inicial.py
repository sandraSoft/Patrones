from adapter.entidades_inicial import Cuenta

class OperacionBancaria:
    """
    Clase que realiza operaciones o transacciones con productos bancarios
    """

    def realizar_retiro(self, cuenta, cantidad):
        """
        Realiza un retiro de una cuenta o producto bancario
        """
        return cuenta.retirar(cantidad)
    
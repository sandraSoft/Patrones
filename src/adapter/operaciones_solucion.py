class OperacionBancaria:
    """
    Clase que realiza operaciones o transacciones con productos bancarios
    """

    def realizar_retiro(self, producto, cantidad):
        """
        Realiza un retiro de un producto bancario
        """
        return producto.retirar(cantidad)
    
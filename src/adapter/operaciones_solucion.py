class OperacionBancaria:
    """
    Clase que realiza operaciones o transacciones con productos bancarios.
    CORRESPONDE AL ROL "Client" DEL PATRÓN ADAPTER.
    """

    def realizar_retiro(self, producto, cantidad):
        """
        Realiza un retiro de un producto bancario
        """
        return producto.retirar(cantidad)
    
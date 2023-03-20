class Apuesta:
    """
    Una apuesta de dinero que puede aumentar o ser cancelada.
    """
    def __init__(self):
        self.cantidad_dinero = 0
        self.estado = "activa"
        
    def incrementar(self):
        """
        En el modo básico, una apuesta se incrementa en un valor fijo.
        """
        if self.estado != "cancelada":
            self.cantidad_dinero += 10000
            
    def cancelar(self):
        """
        Al cancelar una apuesta se le reintegra el valor al apostador,
        y ya no se puede seguir incrementando.
        """
        self.cantidad_dinero = 0
        self.estado = "cancelada"
        
    def __str__(self):
        return f"Dinero = ${self.cantidad_dinero}\nEstado = {self.estado}"
    
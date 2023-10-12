class Carro:
    """
    Información básica de un vehículo, que puede estar originalmente
    en diferentes formatos (por venir de diferentes fuentes).
    """
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo
    
    def __str__(self):
        return "[placa="+self.placa+", modelo="+str(self.modelo)+"]"

class Auto:
    """
    Auto con muchas características opcionales
    """
    placa = None
    marca = None
    tipo = None
    tipo_bateria = None
    asientos = 0
    potencia_motor = 0
    largo = 0
    ancho = 0
    extras = None


class AutoBuilder:
    """
    Un constructor de un auto, que da más flexibilidad que solo el constructor
    """    
    def __init__(self, placa, marca):
        self.auto = Auto()
        self.auto.placa = placa
        self.auto.marca = marca
    
    def tipo(self, tipo):
        self.auto.tipo = tipo
        return self
    
    def tipo_bateria(self, tipo_bateria):
        self.auto.tipo_bateria = tipo_bateria
        return self
    
    def asientos(self, asientos):
        self.auto.asientos = asientos
        return self
    
    def potencia_motor(self, potencia_motor):
        self.auto.potencia_motor = potencia_motor
        return self
    
    def largo(self, largo):
        self.auto.largo = largo
        return self
    
    def ancho(self, ancho):
        self.auto.ancho = ancho
        return self
    
    def extra(self, extra):
        if self.auto.extras is None:
            self.auto.extras = []
        self.auto.extras.append(extra)
        return self
    
    def crear(self):
        return self.auto

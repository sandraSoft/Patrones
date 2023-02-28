class Auto:
    """
    Auto con muchas características opcionales
    """

    def __init__(self, placa, marca, tipo=None, tipo_bateria=None, asientos=0,\
        potencia_motor=0, largo=0, ancho=0, extras=None):
        self.placa = placa
        self.marca = marca
        self.tipo = tipo
        self.tipo_bateria = tipo_bateria
        self.asientos = asientos
        self.potencia_motor = potencia_motor
        self.largo = largo
        self.ancho = ancho
        self.extras = extras
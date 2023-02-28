from fluent_builder.auto_defaults import Auto

class Agencia:
    """
    Agencia que vende autos con diferentes características,
    y envía solo los datos que necesita cada uno para crearlo (en un diccionario).
    """

    def __init__(self):
        self.autos = []
    
    def adicionar_auto(self, datos_auto, extras):
        auto = Auto(**datos_auto, extras=extras)
        self.autos.append(auto)
    
    def buscar_auto(self, placa):
        for auto in self.autos:
            if (auto.placa == placa):
                return auto
        return None
    
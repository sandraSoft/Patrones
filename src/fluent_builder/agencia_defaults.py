from fluent_builder.auto_defaults import Auto

class Agencia:
    """
    Agencia que vende autos
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
    
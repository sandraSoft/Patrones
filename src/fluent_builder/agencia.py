from fluent_builder.auto import Auto

class Agencia:
    """
    Agencia que vende autos
    """

    def __init__(self):
        self.autos = []
    
    def adicionar_auto(self, datos_auto, extras):
        if "tipo" not in datos_auto:
            datos_auto["tipo"] = None
        
        if "tipo_bateria" not in datos_auto:
            datos_auto["tipo_bateria"] = None
        
        if "asientos" not in datos_auto:
            datos_auto["asientos"] = 0

        if "potencia_motor" not in datos_auto:
            datos_auto["potencia_motor"] = 0
        
        if "largo" not in datos_auto:
            datos_auto["largo"] = 0

        if "ancho" not in datos_auto:
            datos_auto["ancho"] = 0

        auto = Auto(datos_auto["placa"],datos_auto["marca"], datos_auto["tipo"], \
            datos_auto["tipo_bateria"], datos_auto["asientos"], \
                datos_auto["potencia_motor"], datos_auto["largo"], datos_auto["ancho"], extras)
        self.autos.append(auto)
    
    def buscar_auto(self, placa):
        for auto in self.autos:
            if (auto.placa == placa):
                return auto
        return None
    
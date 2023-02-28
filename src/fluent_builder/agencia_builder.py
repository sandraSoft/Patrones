from fluent_builder.auto_con_builder import Auto
from fluent_builder.auto_con_builder import AutoBuilder

class Agencia:
    """
    Agencia que vende autos con diferentes características.
    Usa el Fluent Builder para solo crear cada auto con las que necesita.
    """

    def __init__(self):
        self.autos = []
    
    def adicionar_auto(self, datos_auto, extras):
        constructor = AutoBuilder(datos_auto["placa"], datos_auto["marca"])

        if "tipo" in datos_auto:
            constructor.tipo(datos_auto["tipo"])
        
        if "tipo_bateria" in datos_auto:
            constructor.tipo_bateria(datos_auto["tipo_bateria"])

        if "asientos" in datos_auto:
            constructor.asientos(datos_auto["asientos"])
        
        if "potencia_motor" in datos_auto:
            constructor.potencia_motor(datos_auto["potencia_motor"])

        if "largo" in datos_auto:
            constructor.largo(datos_auto["largo"])

        if "ancho" in datos_auto:
            constructor.ancho(datos_auto["ancho"])
        
        if extras != None:
            for extra in extras:
                constructor.extra(extra)

        auto = constructor.crear()
        self.autos.append(auto)
    
    def buscar_auto(self, placa):
        for auto in self.autos:
            if (auto.placa == placa):
                return auto
        return None
    
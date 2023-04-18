class SensorVelocidad:
    """
    Simula un sensor de velocidad de una bicicleta.
    AVISA a las clases Mensaje y VentanaColor cuando la velocidad cambia,
    lo cual la hace dependiente de estas clases y poco flexible
    (en caso de cambiar la forma de informar).
    """

    VELOCIDAD_ALTA = 50
    VELOCIDAD_MEDIA = 35

    def __init__(self,velocidad=0, mensaje=None, ventana_color=None):
        self.velocidad = velocidad
        self.mensaje = mensaje
        self.vantana_color = ventana_color

    def cambiar_velocidad(self, velocidad):
        """
        Cambia la velocidad y llama a los métodos correspondientes
        de Mensaje y VentanaColor para que se actualicen.
        """
        self.velocidad = velocidad
        self.mensaje.mostrar(velocidad)
        self.ventana_color.actualizar_color(self)

class Sensor:
    """
    Representa un dato que es medido u obtenido por un sensor
    y es "observado" por otros que están interesados en tomar acciones
    cuando cambia el valor.

    Representa el rol SUBJECT (Observable) en el patrón Observer:
    - Tiene la lista de observadores y los notifica cuando hay un cambio.
    """
    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)
    
    def notificar(self, sensor):
        """
        Recorre la lista de observadores para informarles que hay un cambio en el valor, 
        para que ellos tomen la acción que corresponda.
        """
        for observador in self.observadores:
            observador.actualizar(sensor)


class SensorVelocidad(Sensor):
    """
    Simula un sensor de velocidad de una bicicleta.
    
    Es hija de Sensor, por lo que es un Observable concreto
    (CONCRETE SUBJECT) en el patrón Observer. 
    No necesita tener referencias a cada clase interesada
    en la velocidad, eso lo hace la clase padre Sensor.
    """

    VELOCIDAD_ALTA = 50
    VELOCIDAD_MEDIA = 35

    def __init__(self,velocidad=0):
        Sensor.__init__(self)
        self.velocidad = velocidad

    def cambiar_velocidad(self, velocidad):
        """
        Cambia la velocidad y llama al método "notificar", 
        para que los interesados se actualicen (parte del patrón Observer).
        """
        self.velocidad = velocidad
        self.notificar(self)

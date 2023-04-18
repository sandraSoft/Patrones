import tkinter as tk
from entidades_solucion import Sensor, SensorVelocidad
from abc import ABC, abstractmethod

class ObservadorSensor(ABC):
    """
    Representa el comportamiento de los OBSERVADORES que son notificados
    cuando cambie algún dato en un sensor (como velocidad de una bicicleta),
    para que se actualicen.
    Corresponde al rol OBSERVER del patrón del mismo nombre.
    """

    @abstractmethod
    def actualizar(self, sensor:Sensor):
        """ 
        Método que se llama cuando cambia el dato del cual se está pendiente
        (como la velocidad).
        """

class Mensaje:
    """ 
    Muestra un mensaje cuando la velocidad de la bicicleta supera un límite.

    Implementa la interfaz "ObserverSensor", por lo que tiene el rol de
    CONCRETE OBSERVER, del patrón Observer
    """

    def mostrar(self, valor_velocidad):
        if (valor_velocidad > SensorVelocidad.VELOCIDAD_ALTA):
            print("Velocidad: ",valor_velocidad)
    
    def actualizar(self, sensor):
        velocidad = sensor.velocidad
        self.mostrar(velocidad)


class VentanaColor(tk.Tk):
    """
    Ventana sencilla para mostrar un color, dependiendo de la velocidad de la bicicleta.

    Implementa la interfaz "ObserverSensor", por lo que tiene el rol de
    CONCRETE OBSERVER, del patrón Observer
    """

    def __init__(self):
        super().__init__()
        self.title("Velocidad bicicleta:")
        self.geometry("445x131+100+250")
        self.contentPane = tk.Frame(self)
        self.contentPane.pack(fill=tk.BOTH, expand=True)
        self.recuadroColor = tk.Label(self.contentPane)
        self.recuadroColor.place(x=138, y=25, width=148, height=39)
        self.recuadroColor.config(relief="solid", borderwidth=1)
        self.recuadroColor.config(background="white")
    
    def actualizar_color(self, sensor):
        """
        Muestra un color en el recuadro, dependiendo de la velocidad de la bicicleta
        para advertir si el valor está dentro de unos rangos aceptables o no.
        Verde: velocidad baja, Amarillo: aceptable (medio), Rojo: muy rápido 
        """
        velocidad_bicicleta = sensor.velocidad
        if velocidad_bicicleta < sensor.VELOCIDAD_MEDIA:
            self.recuadroColor.config(background="green")
            return
        elif velocidad_bicicleta <= sensor.VELOCIDAD_ALTA:
            self.recuadroColor.config(background="yellow")
            return
        self.recuadroColor.config(background="red")

    def actualizar(self, sensor):
        self.actualizar_color(sensor)

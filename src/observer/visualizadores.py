import tkinter as tk
from entidades import SensorVelocidad

class Mensaje:
    """ 
    Muestra un mensaje cuando la velocidad de la bicicleta supera un límite.
    """

    def mostrar(self, valor_velocidad):
        if (valor_velocidad > SensorVelocidad.VELOCIDAD_ALTA):
            print("Velocidad: ",valor_velocidad)


class VentanaColor(tk.Tk):
    """
    Ventana sencilla para mostrar un color, dependiendo de la velocidad de la bicicleta.
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

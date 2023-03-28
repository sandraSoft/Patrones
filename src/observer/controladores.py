import tkinter as tk
import sys
from entidades import SensorVelocidad
from visualizadores import Mensaje, VentanaColor

class VentanaSimulaSensor(tk.Tk):
    """
    Ventana sencilla para ingresar un valor para la velocidad
    de la bicicleta (para hacer pruebas).
    """
    def __init__(self, sensor):
        super().__init__()
        self.sensor = sensor
        self.title("Velocidad bicicleta")
        self.geometry("448x133+100+100")
        self.campo_velocidad = tk.Entry(self)
        self.campo_velocidad.place(x=148, y=41, width=86, height=20)
        lbl_velocidad = tk.Label(self, text="Velocidad:")
        lbl_velocidad.place(x=29, y=44)
        btn_ok = tk.Button(self, text="OK", command=self.cambiar_velocidad)
        btn_ok.place(x=282, y=40, width=89, height=23)

    def cambiar_velocidad(self):
        """
        Obtiene la velocidad ingresada por el usuario y la guarda en el sensor.
        """
        valor_velocidad = float(self.campo_velocidad.get())
        self.sensor.cambiar_velocidad(valor_velocidad)
        self.campo_velocidad.delete(0, tk.END)


class ProgramaSimulador:
    def __init__(self):
        self.sensor = SensorVelocidad()
        self.ventana_color = VentanaColor()

        self.sensor.mensaje = Mensaje()
        self.sensor.ventana_color = self.ventana_color

        self.ventana_pruebas = VentanaSimulaSensor(self.sensor)

        self.ventana_color.deiconify()
        self.ventana_pruebas.deiconify()
        self.ventana_pruebas.mainloop()

if __name__ == "__main__":
    programa = ProgramaSimulador()
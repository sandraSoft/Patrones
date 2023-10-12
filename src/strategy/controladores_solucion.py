import json
from strategy.archivos import LectorArchivo

class ControlCarros:
    """
    Clase que obtiene datos de un archivo para crear una lista de carros. 
    Corresponde al rol CONTEXT en el patrón Strategy.
    """
    def __init__(self, convertidor):
        self.carros = []
        self.convertidor = convertidor
    
    def obtener_datos_carros(self, ruta_archivo):
        """ 
        Crea un lector para obtener los datos de un archivo,
        a partir de su ruta, y obtener los datos de los carros que tiene
        """
        lector = LectorArchivo(ruta_archivo)
        texto_archivo = lector.leer_texto_archivo()
        if texto_archivo is not None:
            self.carros = self.convertidor.crear_lista_carros(texto_archivo)

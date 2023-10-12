import json
from strategy.archivos import LectorArchivo
from strategy.entidades import Carro

class ControlCarros:
    """
    Clase que obtiene datos de un archivo para crear una lista de carros. 
    """
    def __init__(self):
        self.carros = []
    
    def obtener_datos_carros(self, ruta_archivo):
        """ 
        Crea un lector para obtener los datos de un archivo,
        a partir de su ruta, y obtener los datos de los carros que tiene
        """
        lector = LectorArchivo(ruta_archivo)
        texto_archivo = lector.leer_texto_archivo()
        if texto_archivo is not None:
            self.crear_lista_carros(texto_archivo)
    
    def crear_lista_carros(self, texto):
        """ 
        A partir de un texto, que corresponde a un arreglo de objetos JSON,
        se obtienen los datos de carros para crearlos
        y guardarlos en la colección.
        Si el texto no tiene el formato correcto, no se realiza ninguna acción.
        """ 
        try:
            arreglo_json = json.loads(texto)
            for objeto_json in arreglo_json:
                carro = self.crear_carro(objeto_json)
                self.carros.append(carro)
        except json.decoder.JSONDecodeError:
            pass  # si el formato es incorrecto, no se crean carros.
    
    def crear_carro(self, datos):
        """ 
        Crea un objeto Carro a partir de los datos de un diccionario
        (que se obtuvo previamente de un Json)
        """ 
        placa = datos["placa"]
        modelo = datos["modelo"]
        carro = Carro(placa, modelo)
        return carro

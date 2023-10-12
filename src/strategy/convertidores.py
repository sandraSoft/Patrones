import json
from abc import ABC, abstractmethod
from strategy.entidades import Carro

class ConvertidorFormato(ABC):
    """
    Métodos para "convertir" un texto con datos de carros en 
    una lista de objetos Carro.
    Corresponde al rol STRATEGY.
    """

    @abstractmethod
    def crear_lista_carros(self, texto: str) -> list:
        """
        A partir de un texto, que corresponde datos de varios carros,
        se obtienen los datos para crear los objetos "Carro"
        y guardarlos en una lista.
        """
    
    @abstractmethod
    def crear_carro(self, datos: str) -> Carro:
        """ 
        Crea un objeto Carro a partir de los datos de un String.
        """ 


class ConvertidorJson(ConvertidorFormato):
    """ 
    Permite convertir datos de carros que están en formato JSON
    a sus correspondientes objetos "Carro" en Java.
    Corresponde al rol CONCRETE STRATEGY.
    """ 

    def crear_lista_carros(self, texto):
        carros = []
        try:
            arreglo_json = json.loads(texto)
            for objeto_json in arreglo_json:
                carro = self.crear_carro(objeto_json)
                carros.append(carro)
        except json.decoder.JSONDecodeError:
            pass  # si el formato es incorrecto, no se crean carros.
        return carros

    def crear_carro(self, datos):
        placa = datos["placa"]
        modelo = datos["modelo"]
        carro = Carro(placa, modelo)
        return carro


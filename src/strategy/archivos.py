class LectorArchivo:
    """
    Clase relacionada con un archivo de texto, para leer su contenido.
    """

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
    
    def leer_texto_archivo(self):
        """
        Retorna el texto completo del archivo, como una cadena.
        """
        try:
            archivo=open(self.ruta_archivo,"r")
            return archivo.read()
        except FileNotFoundError:
            return None

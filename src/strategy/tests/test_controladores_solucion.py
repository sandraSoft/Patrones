import unittest
from strategy.controladores_solucion import ControlCarros
from strategy.convertidores import ConvertidorJson

class TestControlCarros(unittest.TestCase):
    # ESCRIBIR LA RUTA DE LA CARPETA DONDE ESTÁN LOS ARCHIVOS DE PRUEBA.
    # POR EJEMPLO: C:\\UCaldas\\IngSw\\Patrones\\
    carpeta = "C:\\Sandra\\UCaldas\\datos\\VSCode\\Patrones\\src\\strategy\\resources\\"
    
    def test_archivo_inexistente(self):
        control = ControlCarros(ConvertidorJson())
        control.obtener_datos_carros("INEXISTENTE")
        carros = control.carros
        self.assertEqual(0, len(carros))
    
    def test_formato_incorrecto(self):
        control = ControlCarros(ConvertidorJson())
        control.obtener_datos_carros(TestControlCarros.carpeta+"CarrosIncorrecto.json")
        carros = control.carros
        self.assertEqual(0, len(carros))
    
    def test_archivo_json_valido(self):
        control = ControlCarros(ConvertidorJson())
        control.obtener_datos_carros(TestControlCarros.carpeta+"Carros.json")
        carros = control.carros
        self.assertEqual(2, len(carros))
        self.assertEqual("[placa=QUX-346, modelo=2020]", str(carros[0]))
        self.assertEqual("[placa=HFY-974, modelo=2019]", str(carros[1]))

if __name__ == '__main__':
    unittest.main()
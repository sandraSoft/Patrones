import unittest
from decorator.entidades import Celular

class TestCelular(unittest.TestCase):
    """
    Pruebas del cálculo del precio de un celular con diferentes características.
    """

    def test_celular_base(self):
        celular = Celular("moto",256)
        precio_esperado = 807200
        self.assertEqual(precio_esperado, celular.calcular_precio())

    """
    Estas pruebas todavía no se pueden hacer:
    
    def test_celular_usado(self):
        celular_usado = CelularUsado(Celular("moto",256))
        precio_esperado = 403600
        self.assertEqual(precio_esperado, celular_usado.calcular_precio())

    def test_celular_con_camara(self):
        celular_con_camara = CelularCamara(Celular("moto",256))
        precio_esperado = 968640
        self.assertEqual(precio_esperado, celular_con_camara.calcular_precio())

    def test_celular_usado_con_camara(self):
        celular_con_camara = CelularCamara(CelularUsado(Celular("moto",256)))
        precio_esperado = 484320
        self.assertEqual(precio_esperado, celular_con_camara.calcular_precio())

    """
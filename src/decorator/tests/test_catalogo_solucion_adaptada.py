import unittest
from decorator.catalogo import Catalogo
from decorator.entidades_solucion_adaptada import Celular
from decorator.entidades_solucion_adaptada import CelularUsado
from decorator.entidades_solucion_adaptada import CelularCamara

class TestCelular(unittest.TestCase):
    """
    Pruebas para calcular el valor total del catálogo con varios celulares.
    """

    def test_catalogo_vacio(self):
        catalogo = Catalogo()
        self.assertEqual(0, catalogo.get_precio_total_catalogo())

    def test_catalogo_varios_celulares(self):
        catalogo = Catalogo()
        catalogo.adicionar_celular(Celular("LG",256))
        catalogo.adicionar_celular(CelularUsado(Celular("Moto",256)))
        catalogo.adicionar_celular(CelularCamara(Celular("Samsung",128)))
        precio_esperado = 1995120
        self.assertEqual(precio_esperado, catalogo.get_precio_total_catalogo())

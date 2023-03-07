import unittest
from decorator.catalogo import Catalogo
from decorator.entidades import CelularBase

class TestCelular(unittest.TestCase):
    """
    Pruebas para calcular el valor total del catálogo con varios celulares.
    """

    def test_catalogo_vacio(self):
        catalogo = Catalogo()
        self.assertEqual(0, catalogo.get_precio_total_catalogo())

    def test_catalogo_celulares_base(self):
        catalogo = Catalogo()
        catalogo.adicionar_celular(CelularBase("LG",256))
        catalogo.adicionar_celular(CelularBase("Moto",256))
        precio_esperado = 1614400
        self.assertEqual(precio_esperado, catalogo.get_precio_total_catalogo())

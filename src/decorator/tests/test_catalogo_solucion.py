import unittest
from decorator.catalogo import Catalogo
from decorator.entidades_solucion import *

class TestCelular(unittest.TestCase):
    """
    Pruebas para calcular el valor total del catálogo con varios celulares.
    """

    def test_catalogo_vacio(self):
        catalogo = Catalogo()
        self.assertEqual(0, catalogo.get_precio_total_catalogo())

    def test_catalogo_varios_celulares(self):
        catalogo = Catalogo()
        catalogo.adicionar_celular(CelularBase("LG",256))
        catalogo.adicionar_celular(Usado(CelularBase("Moto",256)))
        catalogo.adicionar_celular(ConCamara(CelularBase("Samsung",128)))
        precio_esperado = 1995120
        self.assertEqual(precio_esperado, catalogo.get_precio_total_catalogo())

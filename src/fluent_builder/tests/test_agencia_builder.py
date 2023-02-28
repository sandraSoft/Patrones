import unittest
from fluent_builder.agencia_builder import Agencia

class TestAgencia(unittest.TestCase):
    """
    Pruebas de una agencia de autos, para adicionar y buscar un auto
    """

    def test_adicionar_y_buscar_auto(self):
        agencia = Agencia()
        datos_auto = {"placa":"KWE-568","marca":"Nissan Burbuja", "tipo":"SUV",\
            "largo":3100}
        agencia.adicionar_auto(datos_auto, None)
        auto = agencia.buscar_auto("KWE-568")

        self.assertEqual("KWE-568", auto.placa)
        self.assertEqual("Nissan Burbuja", auto.marca)
        self.assertEqual("SUV",auto.tipo)
        self.assertIsNone(auto.tipo_bateria)
        self.assertEqual(0, auto.asientos)
        self.assertEqual(0, auto.potencia_motor)
        self.assertEqual(3100, auto.largo)
        self.assertEqual(0, auto.ancho)
        self.assertIsNone(auto.extras)


    def test_buscar_auto_no_existe(self):
        agencia = Agencia()
        auto = agencia.buscar_auto("ZZZ")
        self.assertIsNone(auto)
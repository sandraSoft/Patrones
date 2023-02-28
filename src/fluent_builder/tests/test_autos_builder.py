import unittest
from fluent_builder.auto_con_builder import Auto
from fluent_builder.auto_con_builder import AutoBuilder

class TestAuto(unittest.TestCase):
    """
    Pruebas para crear un auto con todos los parámetros
    """

    def test_auto_completo(self):
        auto = AutoBuilder("QWE-123","Renault Sandero").tipo("SUV").tipo_bateria("Litio").\
            asientos(5).potencia_motor(250).largo(3000).ancho(1200).\
                extra("GPS").extra("Bloqueo central").crear()
        
        self.assertEqual("QWE-123", auto.placa)
        self.assertEqual("Renault Sandero", auto.marca)
        self.assertEqual("SUV", auto.tipo)
        self.assertEqual("Litio", auto.tipo_bateria)
        self.assertEqual(5, auto.asientos)
        self.assertEqual(250, auto.potencia_motor)
        self.assertEqual(3000, auto.largo)
        self.assertEqual(1200, auto.ancho)
        self.assertEqual(["GPS", "Bloqueo central"], auto.extras)
    
    def test_auto_pocos_valores(self):
        auto = AutoBuilder("THW-489","KIA Sport").crear()

        self.assertEqual("THW-489", auto.placa)
        self.assertEqual("KIA Sport", auto.marca)
        self.assertIsNone(auto.tipo)
        self.assertIsNone(auto.tipo_bateria)
        self.assertEqual(0, auto.asientos)
        self.assertEqual(0, auto.potencia_motor)
        self.assertEqual(0, auto.largo)
        self.assertEqual(0, auto.ancho)
        self.assertIsNone(auto.extras)
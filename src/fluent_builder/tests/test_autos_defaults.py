import unittest
from fluent_builder.auto_defaults import Auto

class TestAuto(unittest.TestCase):
    """
    Pruebas para crear un auto con diferentes argumentos en el constructor.
    """

    def test_auto_completo(self):
        auto = Auto("QWE-123","Renault Sandero","SUV","Litio",
				5,250,3000,1200,["GPS", "Bloqueo central"])
        
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
        auto = Auto("THW-489","KIA Sport",asientos=5)

        self.assertEqual("THW-489", auto.placa)
        self.assertEqual("KIA Sport", auto.marca)
        self.assertIsNone(auto.tipo)
        self.assertIsNone(auto.tipo_bateria)
        self.assertEqual(5, auto.asientos)
        self.assertEqual(0, auto.potencia_motor)
        self.assertEqual(0, auto.largo)
        self.assertEqual(0, auto.ancho)
        self.assertIsNone(auto.extras)

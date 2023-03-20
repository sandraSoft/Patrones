import unittest
from command.modelo import Apuesta

class TestApuesta(unittest.TestCase):
    ACTIVA = "activa"
    CANCELADA = "cancelada"

    def test_incrementar_apuesta(self):
        apuesta = Apuesta()
        self.assertEqual(0,apuesta.cantidad_dinero)
        self.assertEqual(self.ACTIVA,apuesta.estado)
        apuesta.incrementar()
        self.assertEqual(10000,apuesta.cantidad_dinero)
        self.assertEqual(self.ACTIVA,apuesta.estado)

    def test_cancelar_apuesta(self):
        apuesta = Apuesta()
        self.assertEqual(0,apuesta.cantidad_dinero)
        self.assertEqual(self.ACTIVA,apuesta.estado)
        apuesta.cancelar()
        self.assertEqual(0,apuesta.cantidad_dinero)
        self.assertEqual(self.CANCELADA,apuesta.estado)
    
    def test_incrementar_apuesta_cancelada(self):
        apuesta = Apuesta()
        self.assertEqual(0,apuesta.cantidad_dinero)
        self.assertEqual(self.ACTIVA,apuesta.estado)
        apuesta.cancelar()
        apuesta.incrementar()
        self.assertEqual(0,apuesta.cantidad_dinero)
        self.assertEqual(self.CANCELADA,apuesta.estado)

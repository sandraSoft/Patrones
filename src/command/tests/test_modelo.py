import unittest
from command.modelo import Apuesta

class TestApuesta(unittest.TestCase):

    DINERO_CERO = "Dinero = $0\n"
    ACTIVA = "Estado = activa"
    CANCELADA = "Estado = cancelada"

    def test_incrementar_apuesta(self):
        apuesta = Apuesta()
        self.assertEqual(self.DINERO_CERO+self.ACTIVA,str(apuesta))
        apuesta.incrementar()
        self.assertEqual("Dinero = $10000\n"+self.ACTIVA,str(apuesta))

    def test_cancelar_apuesta(self):
        apuesta = Apuesta()
        self.assertEqual(self.DINERO_CERO+self.ACTIVA,str(apuesta))
        apuesta.cancelar()
        self.assertEqual(self.DINERO_CERO+self.CANCELADA,str(apuesta))
    
    def test_incrementar_apuesta_cancelada(self):
        apuesta = Apuesta()
        self.assertEqual(self.DINERO_CERO+self.ACTIVA,str(apuesta))
        apuesta.cancelar()
        apuesta.incrementar()
        self.assertEqual(self.DINERO_CERO+self.CANCELADA,str(apuesta))

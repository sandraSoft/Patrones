import unittest
from adapter.entidades_solucion_simplificada import Cuenta
from adapter.entidades_solucion_simplificada import TarjetaCredito

class TestCuenta(unittest.TestCase):
    """
    Se prueba el método retirar de una Cuenta bancaria, verificando
    que valide valores negativos o mayores al saldo.
    """

    def test_retirar_normal(self):
        cuenta = Cuenta("123", 800000)
        saldo_esperado = 200000

        resultado_retiro = cuenta.retirar(600000)
        self.assertTrue(resultado_retiro)
        self.assertEqual(saldo_esperado, cuenta.saldo)
    
    def test_retirar_negativo(self):
        cuenta = Cuenta("456", 300000)
        saldo_esperado = 300000
        
        resultado_retiro = cuenta.retirar(-400000)
        self.assertFalse(resultado_retiro)
        self.assertEqual(saldo_esperado, cuenta.saldo)

    def test_retirar_mas_del_saldo(self):
        cuenta = Cuenta("789", 500000)
        saldo_esperado = 500000
        
        resultado_retiro = cuenta.retirar(700000)
        self.assertFalse(resultado_retiro)
        self.assertEqual(saldo_esperado, cuenta.saldo)


class TestTarjetaCredito(unittest.TestCase):
    """
    Se prueba el método de realizar avance de una Tarjeta de crédito, verificando
    que valide valores negativos o mayores al valor.
    """

    def test_avance_normal(self):
        tarjeta = TarjetaCredito("123", 800000)
        valor_esperado = 200000

        tarjeta.realizar_avance(600000)
        self.assertEqual(valor_esperado, tarjeta.valor)

    def test_avance_negativo(self):
        tarjeta = TarjetaCredito("456", 300000)
        valor_esperado = 300000

        with self.assertRaises(ValueError):
            tarjeta.realizar_avance(-400000)
        self.assertEqual(valor_esperado, tarjeta.valor)

    def test_avance_mas_del_valor(self):
        tarjeta = TarjetaCredito("789", 500000)
        valor_esperado = 500000

        with self.assertRaises(ValueError):
            tarjeta.realizar_avance(700000)
        self.assertEqual(valor_esperado, tarjeta.valor)

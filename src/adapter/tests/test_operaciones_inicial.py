import unittest
from adapter.operaciones_inicial import OperacionBancaria
from adapter.entidades_inicial import Cuenta

class TestOperacionBancaria(unittest.TestCase):
    """
    Se prueba la funcionalidad de realizarRetiro, para productos bancarios.

    POR AHORA SOLO FUNCIONA PARA CUENTAS.
    TODAVÍA NO SE PUEDEN HACER "RETIROS" DE TARJETAS DE CRÉDITO.
    """

    def test_retirar_cuenta_normal(self):
        control_banco = OperacionBancaria()
        cuenta = Cuenta("123", 800000)

        resultado_retiro = control_banco.realizar_retiro(cuenta, 600000)
        self.assertTrue(resultado_retiro)
    
    def test_retirar_cuenta_negativo(self):
        control_banco = OperacionBancaria()
        cuenta = Cuenta("456", 300000)

        resultado_retiro = control_banco.realizar_retiro(cuenta, -400000)
        self.assertFalse(resultado_retiro)
    
    def test_retirar_cuenta_mas_del_saldo(self):
        control_banco = OperacionBancaria()
        cuenta = Cuenta("789", 500000)

        resultado_retiro = control_banco.realizar_retiro(cuenta, 700000)
        self.assertFalse(resultado_retiro)
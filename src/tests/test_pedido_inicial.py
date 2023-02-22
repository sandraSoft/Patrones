import unittest
from simple_factory.pedido_inicial import Pedido

class TestPedido(unittest.TestCase):
    
    def test_calcular_precio_balon(self):
        pedido = Pedido()
        pedido.adicionar_juguete(20000, 20, 'b')
        valor_esperado = 23000
        valor_obtenido = pedido.calcular_precio()
        self.assertEqual(valor_esperado, valor_obtenido)

    def test_calcular_precio_peluche(self):
        pedido = Pedido()
        pedido.adicionar_juguete(30000, 50, 'p')
        valor_esperado = 37000
        valor_obtenido = pedido.calcular_precio()
        self.assertEqual(valor_esperado, valor_obtenido)

if __name__ == '__main__':
    unittest.main()
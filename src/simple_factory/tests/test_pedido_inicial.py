import unittest
from simple_factory.pedido_inicial import Pedido

class TestPedido(unittest.TestCase):
    
    def test_calcular_precio_balon(self):
        pedido = Pedido()
        pedido.adicionar_juguete("Balón de baloncesto", 20000, 20, 'b')
        valor_esperado = 23000
        valor_obtenido = pedido.calcular_precio()
        self.assertEqual(valor_esperado, valor_obtenido)

    def test_calcular_precio_muneco(self):
        pedido = Pedido()
        pedido.adicionar_juguete("Linterna verde", 30000, 50, 'm')
        valor_esperado = 37000
        valor_obtenido = pedido.calcular_precio()
        self.assertEqual(valor_esperado, valor_obtenido)
    
    def test_calcular_precio_tren(self):
        pedido = Pedido()
        pedido.adicionar_juguete("Tren de animales", 30000, 50, 't')
        valor_esperado = 67000
        valor_obtenido = pedido.calcular_precio()
        self.assertEqual(valor_esperado, valor_obtenido)
    
    def test_calcular_precio_varios(self):
        pedido = Pedido()
        pedido.adicionar_juguete("Tren de animales", 30000, 50, 't')
        pedido.adicionar_juguete("Linterna verde", 30000, 50, 'm')
        pedido.adicionar_juguete("Balón de baloncesto", 20000, 20, 'b')
        valor_esperado = 123000
        valor_obtenido = pedido.calcular_precio()
        self.assertEqual(valor_esperado, valor_obtenido)
    
    def test_juguete_repetido(self):
        pedido = Pedido()
        pedido.adicionar_juguete("Gallo Claudio", 12000, 50, 'm')
        with self.assertRaises(ValueError):
            pedido.adicionar_juguete("Gallo Claudio", 10000, 50, 'm')
    
    def test_tipo_incorrecto(self):
        pedido = Pedido()
        with self.assertRaises(ValueError):
            pedido.adicionar_juguete("Balón de fútbol", 12000, 20, 'z')


if __name__ == '__main__':
    unittest.main()
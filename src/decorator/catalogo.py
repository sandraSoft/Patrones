class Catalogo:
    """
    Conjunto de celulares que se tienen para la venta.
    """
    def __init__(self):
        self.celulares = []
    
    def adicionar_celular(self, celular):
        self.celulares.append(celular)
    
    def get_precio_total_catalogo(self):
        precio_total = 0
        for celular in self.celulares:
            precio_total += celular.calcular_precio()
        return precio_total

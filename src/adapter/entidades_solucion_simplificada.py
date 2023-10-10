
"""
Productos financieros de una entidad, que se manejan de manera
uniforme al retirar, gracias al patrón Adapter.
"""

class Cuenta():
    """
    Cuenta bancaria de la cual se pueden hacer retiros de dinero.
    CORRESPONDE AL ROL "Target" DEL PATRÓN ADAPTER.
    """
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
    
    def retirar(self, cantidad):
        """
        Sacar dinero de la cuenta, disminuyendo el saldo, siempre y cuando
        la cantidad que se desea retirar sea menor o igual al saldo,
        porque estas cuentas no permiten sobregiros (saldos negativos).
        """
        if (cantidad <= 0) or (cantidad > self.saldo):
            return False
        else:
            self.saldo -= cantidad
            return True


class TarjetaCredito:
    """
    Tarjeta que permite compras a crédito y realiza avances (parecido a retirar dinero).
    CORRESPONDE AL ROL "Adaptee" (o "Service") DEL PATRÓN ADAPTER.
    """
    def __init__(self, numero, valor):
        self.numero = numero
        self.valor = valor
    
    def realizar_avance(self, cantidad):
        """
        Realiza un avance, es decir, retira dinero a cargo de la tarjeta,
        lo cual hace que disminuya su valor.
        La cantidad solicitada debe ser menor o igual al saldo, porque es el cupo permitido.
        """
        if (cantidad <= 0) or (cantidad > self.valor):
            raise ValueError("Cantidad negativa o mayor al saldo")
        
        self.valor -= cantidad


class TarjetaCuenta(Cuenta):
    """
    Permite usar las tarjetas de crédito como cuentas,
    especialmente para usar la función "retirar".
    CORRESPONDE AL ROL "Adapter" DEL PATRÓN ADAPTER.

    Al heredar de Cuenta tiene toda la estructura de esa clase,
    incluso atributos y métodos que no requiere para hacer la adaptación.
    """
    def __init__(self, tarjeta):
        Cuenta.__init__(self, tarjeta.numero, tarjeta.valor)
        self.tarjeta = tarjeta
    
    def retirar(self, cantidad):
        try:
            self.tarjeta.realizar_avance(cantidad)  
            return True
        except ValueError:
            return False
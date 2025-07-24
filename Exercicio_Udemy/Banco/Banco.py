import Cliente
import Conta

class Banco:
    
    def __init__(self, conta: Conta.Conta, cliente: Cliente.Cliente) -> None:
        self.conta: Conta.Conta = conta
        self.cliente: Cliente.Cliente = cliente
        
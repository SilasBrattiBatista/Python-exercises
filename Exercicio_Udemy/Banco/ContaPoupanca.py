import Conta

class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        self.saldo -= valor
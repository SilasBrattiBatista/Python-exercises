import Conta

class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        
        if (self.saldo - valor) < 0:
            print("Valor insuficiente para saque")
        else:
            self.saldo -= valor
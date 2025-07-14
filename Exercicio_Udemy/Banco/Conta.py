from abc import ABC, abstractmethod

class Conta:
    
    def __init__(self, saldo: float, agencia: int, numeroConta: int) -> None:
        self.saldo = saldo
        self.agencia = agencia
        self.numeroConta = numeroConta
        
    @abstractmethod
    def sacar(self, valor: float) -> None:
        self.saldo -= valor
        self.detalhes()
        
    def depositar(self, valor: float) -> None:
        self.saldo += valor
        self.detalhes()
        
    def detalhes(self, msg: str =''):
        print(f"O saldo atual é {self.saldo} {msg}")
        
class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        
        if (self.saldo - valor) < 0:
            print("Valor insuficiente para saque")
        else:
            self.saldo -= valor
            
class ContaCorrente(Conta):
    
    def __init__(self, saldo, agencia, numeroConta, saqueLimite):
        super().__init__(saldo, agencia, numeroConta)
        self.saqueLimite = saqueLimite
    
    def sacar(self, valor):
        
        if (self.saldo - valor) <= -self.saqueLimite:
            print("Valor insuficiente para saque")
            return self.saldo
        
        self.saldo -= valor
        self.detalhes()
        
c1 = ContaCorrente(100, 12, 13, 300)

c1.depositar(100)
c1.sacar(300)
c1.sacar(300)
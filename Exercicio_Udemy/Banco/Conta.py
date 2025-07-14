from abc import ABC, abstractmethod

class Conta:
    
    def __init__(self, saldo, agencia, numeroConta):
        self.saldo = saldo
        self.agencia = agencia
        self.numeroConta = numeroConta
        
    @abstractmethod
    def sacar(self, valor):
        self.saldo -= valor
        self.detalhes()
        
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()
        
    def detalhes(self, msg=''):
        print(f"O saldo atual é {self.saldo} {msg}")
        
class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        
        if (self.saldo - valor) < 0:
            print("Valor insuficiente para saque")
        else:
            self.saldo -= valor
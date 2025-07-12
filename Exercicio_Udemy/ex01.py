"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractclassmethod, abstractmethod

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
        

class ContaCorrente(Conta):
    
    def sacar(self, valor):
        if ((self.saldo - valor) < -300):
            print("Valor insuficiente para sacar")
        else:
            self.saldo -= valor
            
    def depositar(self, valor):
        self.saldo += valor
    
class ContaPoupanca(Conta):
    ...

c1 = ContaCorrente(1000)


print(c1.saldo)
c1.sacar(500)

print(c1.saldo)
c1.sacar(700)

print(c1.saldo)

c1.depositar(200)
print(c1.saldo)
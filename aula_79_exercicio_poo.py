from abc import ABC, abstractmethod
from typing import Union

"""Exercício com Abstração, Herança, Encapsulamento e Polimorfismo.

Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. 
Banco tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
Pessoa tem nome e idade (com getters e setters)
Cliente tem conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
ContaCorrente deve ter um limite extra
Contas têm agência, número da conta e saldo
Contas devem ter método para depósito
Conta (super classe) deve ter método sacar abstrato (abstração e
polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para Agregar classes de clientes e de contas (agregação)
Banco será responsável por autenticar o cliente e as contas da seguinte maneira:
Banco tem contas e clientes (agregação)
* Checar se a agência é daquele banco
* Checar se o cliente é daquele banco
* Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""


class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo: Union[int, float]):
        self.__agencia = agencia
        self.__numero_conta = numero_conta
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @property
    def numero_conta(self):
        return self.__numero_conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @abstractmethod
    def sacar(self, valor_saque):
        pass

    def depositar(self, valor_deposito: Union[float, int]):
        if valor_deposito > 0:
            self.__saldo += valor_deposito
            print(f'Depositou R$ {valor_deposito:.2f}.')
        else:
            print('Você não pode depositar um valor negativo.')

    def desc(self):
        print(f'Agência: {self.agencia}\n'
              f'Conta: {self.numero_conta}\n'
              f'Saldo: R$ {self.saldo:.2f}'
              )


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = -limite

    # Consegue sacar abaixo de zero
    def sacar(self, valor_saque):
        if (self.saldo - valor_saque) >= self.limite:
            self.saldo -= valor_saque
            print(f'Saque de R$ {valor_saque:.2f} realizado.')
            self.desc()
        else:
            print('Transação não realizada, o valor informado excede o limite.')


class ContaPoupanca(Conta):
    def sacar(self, valor_saque):
        if self.saldo > valor_saque:
            self.saldo -= valor_saque
            print(f'Saque de R$ {valor_saque:.2f} realizado.')
            self.desc()
        else:
            print('Você não tem saldo suficiente.')


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @idade.setter
    def idade(self, idade):
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.__conta = None

    @property
    def conta(self):
        return self.__conta

    def definir_conta(self, conta):
        if self.__conta is None:
            self.__conta = conta
        else:
            print('O cliente já possui um conta.')


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333, 4444]
        self.contas = []
        self.clientes = []
        self.autenticado = False

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def cadastrar_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        self.autenticado = False
        if cliente not in self.clientes:
            print('Erro! Cliente não cadastrado.')
        elif cliente.conta.agencia not in self.agencias:
            print('Erro! Agência inválida.')
        elif cliente.conta not in self.contas:
            print('Erro! Conta não cadastrada.')
        else:
            self.autenticado = True

    def efetuar_saque(self, cliente, valor):
        self.autenticar(cliente)
        if self.autenticado:
            cliente.conta.sacar(valor)
        else:
            print('Dados inconsistentes.')


banco_nb = Banco()

cliente_a = Cliente('Joseff', 35)

c_corrente = ContaCorrente(1111, 2873682, 1000, 100)

cliente_a.definir_conta(c_corrente)

banco_nb.cadastrar_cliente(cliente_a)
banco_nb.cadastrar_conta(c_corrente)
banco_nb.efetuar_saque(cliente_a, 500)
banco_nb.efetuar_saque(cliente_a, 240)

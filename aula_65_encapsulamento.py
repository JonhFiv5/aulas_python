# O encapsulamento em Python funciona de forma diferente do que acontece
# em outras linguagens com um foco maior em POO, como Java. Por Python ser mais
# "livre" não temos modificadores de acesso, por exemplo, como o public, private
# ou protected

# De acordo com a filosofia do Python
# todos os desenvolvedores são adultos responsáveis. Então a linguagem não nos
# impede de acessar e modificar algo que deveria ser privado, mas o
# desenvolvedor vai estar fazendo isso por sua conta e risco.

# Há convenções de nomenclatura para atributos e métodos que desejamos que
# sejam privados, se o desenvolvedor não vai seguir a recomendação que demos é
# problema dele :D

# Para indicar fortemente que algo deveria ser privado iniciamos o atributo ou
# método com _
# Ao fazer isso ele ainda continuará sendo público, já que é só recomendação

# Para indicar bem mais fortemente iniciamos com __
# Ao fazer isso um atributo continuará sendo público,
# mas irá sofrer um name mangling, ou seja, o Python irá modificar o nome dele
# Então a forma de acessar muda um pouco, sendo: _NomeClasse__atributo


class CaixaRegistradora:

    def __init__(self, senha):
        self._vendas = {}
        self.__dinheiro = 0
        self.__senha = str(senha)

    @property
    def vendas(self):
        # Como o atributo deve ser privado e o método não, não utilizamos o _
        return self._vendas

    @property
    def dinheiro(self):
        senha_digitada = str(input('Digite a senha: '))
        return self.__dinheiro if senha_digitada == self.__senha else 'Negado'

    def passar_produto(self, produto, valor):
        self._vendas.update({produto: valor})
        self.__dinheiro += valor

    def listar_vendas(self):
        for produto, valor in self._vendas.items():
            print(f'{produto} R${valor:.2f}')


caixa = CaixaRegistradora('Pedrim231')
caixa.passar_produto('Queijo', 17.55)
caixa.passar_produto('Goiabada', 6.5)
caixa.listar_vendas()
print(caixa.dinheiro)
# print(caixa._vendas)  Acessando um valor protegido
# print(caixa._CaixaRegistradora__dinheiro)  Acessando um valor privado

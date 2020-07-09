class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    # Getters ------------------------------------------------------------------
    # Os getters possuem o decorador @property definidos acima deles
    # outra particularidade, tanto em getters quanto setters, é um underscore
    # antes do nome do atributo no momento de retorno ou atribuição de valores
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    # Os getters possuem um comportamento curioso, não lembro se é assim
    # nas outras linguagens, a partir do momento que definimos um getter, sempre
    # que aquele atributo for acessado, ex: self.nome, seja diretamente acessado
    # por uma instância ou dentro de um método de instância, o valor que estamos
    # pegando não é diretamente o valor que foi salvo na variável com o setter,
    # mas sim o valor que é processado pelo getter. O que significa que sempre
    # que fizermos self.atributo, seja em qual local for, implicitamente sempre
    # será chamado o getter daquele atributo.

    # Setters --------------------------------
    # Os setters por sua vez possuem uma característica diferente
    # o decorador que recebem é formado com a sintaxe: @nome_atributo.setter
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @preco.setter
    def preco(self, preco):
        if isinstance(preco, str):
            preco.replace('R$', '')
        self._preco = float(preco)

    # Demais métodos --------------------------
    def desconto(self, percentual):
        self.preco *= 1 - (percentual / 100)

    def descricao(self):
        print(f'{self.nome} -> R$ {self.preco:.2f}')


p1 = Produto('Camiseta', 50)
p1.desconto(10)

p2 = Produto('Smartphone', 900)
p2.desconto(8)

p1.descricao()
p2.descricao()

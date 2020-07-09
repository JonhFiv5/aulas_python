class Produto:
    produtos_cadastrados = 0

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        Produto.produtos_cadastrados += 1

    def descreve_produto(self):
        # Um método de instância precisa ter um objeto para que possa
        # ser chamado
        print(f'{self.nome} R${self.preco:.2f} Quantidade = {self.quantidade}')

    @classmethod
    def numero_produtos(cls):
        # Um método da classe pode ser utilizado por instâncias da classe
        # e pela própria classe em si. Dentro dele temos acesso apenas às
        # variáveis que pertencem à classe e também aos outros classmethods
        print(f'Foram cadastrados {cls.produtos_cadastrados} produtos')

    # Também podemos usar o classmethod para criar uma fábrica de instâncias
    @classmethod
    def produto_desconto(cls, nome, preco, desconto, quantidade):
        preco = preco * (1 - (desconto / 100))
        # Criamos e retornamos um produto já com o desconto aplicado
        return cls(nome, preco, quantidade)


# Chamando o método da classe pela classe
Produto.numero_produtos()
prod_1 = Produto('Queijo', 24.75, 10)
prod_2 = Produto('Queijo', 24.75, 10)
prod_3 = Produto('Queijo', 24.75, 10)

# Chamando o método da classe por uma instância
prod_2.numero_produtos()

Produto.numero_produtos()

# Criando um produto através de um classmethod
prod_4 = Produto.produto_desconto('Abacate', 5, 10, 7)
prod_4.descreve_produto()
Produto.numero_produtos()

# Quando chamamos um método de instância diretamente através da classe ele
# vai ter o self vazio, já que não foi um objeto que o chamou.
# Podemos então passar manualmente um objeto (já existente) para ele, o
# que não faz nenhum sentido, mas é possível
Produto.descreve_produto(prod_1)  # self = prod_1

# Produto.descreve_produto(prod_1) é o mesmo que prod_1.descreve_produto()

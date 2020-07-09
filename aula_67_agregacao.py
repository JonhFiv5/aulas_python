# Agregação é uma relação um pouco mais forte, onde temos duas classes,
# por exemplo, e uma é em parte dependente da outra (essa outra por sua vez
# pode ser totalmente independente). Ou seja, ambas as classes podem existir
# individualmente, mas para o total funcionamento de uma delas são necessárias
# características da outra.

# Por exemplo, um carrinho de compras e um produto podem existir perfeitamente
# um sem o outro. Mas um carrinho sem produtos é algo meio inútil,
# é insuficiente para cumprir sua função.


class CarrinhoDeCompras:

    def __init__(self):
        self.produtos = []
        self.__total = 0

    @property
    def total(self):
        return self.__total

    def inserir_produto(self, produto):
        self.produtos.append(produto)
        self.__total += produto.valor

    def remover_produto(self, nome_produto):
        for cod, produto in enumerate(self.produtos):
            if produto.nome.lower() == nome_produto.lower():
                self.__total -= produto.valor
                del self.produtos[cod]

    def listar_produtos(self):
        print('\nProdutos em seu carrinho de compras: ')
        for produto in self.produtos:
            print(produto.nome.title())
        print(f'\nValor total: R${self.__total:.2f}')


class Produto:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def aplicar_desconto(self, percentual):
        self.valor *= 1 - (percentual / 100)

    def aplicar_aumento(self, percentual):
        self.valor *= 1 + (percentual / 100)


meu_carrinho = CarrinhoDeCompras()

prod_01 = Produto('Carregador', 55)
prod_02 = Produto('Bicicleta', 710)
prod_03 = Produto('Colchão', 300)

meu_carrinho.inserir_produto(prod_01)
meu_carrinho.inserir_produto(prod_02)
meu_carrinho.inserir_produto(prod_03)

meu_carrinho.listar_produtos()

meu_carrinho.remover_produto('carregador')

meu_carrinho.listar_produtos()

# Observe que as duas classes podem existir por si só, mas enquanto a classe
# Produto consegue executar todas as suas funções sem depender do carrinho, a
# classe CarrinhoDeCompras praticamente é um peso morto sem produto, pois todas
# as suas funções estão ligadas a isso.

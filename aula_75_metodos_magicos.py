# Métodos mágicos nos permitem realizar praticamente qualquer coisa em Python
# Eles nos permitem mudar o comportamento padrão da linguagem, por exemplo
# Um exemplo de métodos mágicos foram vistos no arquivo anterior, onde
# alteramos o comportamento dos operadores dentro de classes

# Os métodos mágicos são envolvidos por underscores duplos
# Um dos métodos mágicos mais conhecidos é o __init__, que nos permite definir
# um comportamento para ser executado quando criamos uma instânca

# Entretanto o método __init__ não é a primeira coisa a ser executada quando
# criamos uma instância, mas sim o método __new__
# Em Python não possuimos um construtor, mas pode-se dizer que esses dois
# métodos juntos atuam como um.

# Estrutura padrão do __new__:
# def __new__(cls, *args, **kwargs):
#     return super().__new__(cls)


# Através da alteração do new podemos usar o design pattern singleton, por
# exemplo, esse padrão é utilizado em classes que devem ter
# apenas uma instância
# Então ao rodar o init, se uma instância já tiver sido criada será retornada
# ela ao invés de criar uma nova

class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_criada'):
            cls._criada = super().__new__(cls)
        return cls._criada

    def __init__(self):
        pass


primeira_instancia = A()

# Como só é permitida ter uma instância, essas duas abaixo vão receber a
# primeira instância que foi criada. Ou seja, todas elas são as mesmas.
copia_instancia_a = A()
copia_instancia_b = A()

print(id(primeira_instancia))
print(id(copia_instancia_a))
print(id(copia_instancia_b))


# Alterando o comportamento da igualdade ==
# Se compararmos diretamente duas instância o que é comparado por padrão é o
# endereço na memória e não seus valores. Então podemos personalizar isso
# alterando o método mágico __eq__


class Medidas:
    def __init__(self, altura, largura):
        self.largura = largura
        self.altura = altura

    def __eq__(self, other):
        if self.altura == other.altura and self.largura == other.largura:
            return True
        else:
            return False


medidas_a = Medidas(10, 5)
medidas_b = Medidas(10, 5)

print(medidas_a == medidas_b)

# Isso também pode ser feito com todos os outros operadores relacionais,
# aritméticos, etc. Há vários métodos mágicos.

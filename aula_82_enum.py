# O enum é usado quando queremos usar um valor entre valores pré-definidos
# Como um 'menu', não podemos selecionar uma opção que não exista nele

from enum import Enum, auto
# Criamos uma classe que herda de Enum. O método auto() vai gerar valores
# automaticamente, começando de 1. Isso pode ser útil quando precisamos ter
# várias opções. Ás vezes nem precisamos usar o valor.


class Menu(Enum):
    # Basta isso para criar um enum. No lugar de auto() poderíamos passar os
    # valores que quisermos, como variáveis comuns
    macarrao = auto()
    sopa = auto()
    lasanha = auto()
    salada = auto()


def pedir(prato):
    # Podemos verificar se o prato faz parte do nosso Enum
    if not isinstance(prato, Menu):
        raise ValueError('Esse prato não existe em nosso cardápio.')
    else:
        # Pegamos o nome e o valor acessando as propriedades name e value
        print(f'Entendido, saindo o prato n° {prato.value}, {prato.name}.')


# Acessamos a opção como acessamos uma variável de classe
pedir(Menu.lasanha)
pedir('Queijo')  # Não faz parte das opções disponíveis, cai na excessão

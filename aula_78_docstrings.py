# Documentação é envolvida com três aspas duplas
# """Documentação de uma linha"""

"""Documentação de várias linhas, contém uma breve descrição sobre o módulo.

aksndlaksn ksdnl nskln l nkdn kan ksjlnlak
fgjn jkn jknkjnskdjjkn  kajnkjn akjn jkaan
noan anqijnwh wjh qkkkkqi oqoiw kjanpoqjp qln q

"""

# Strings de várias linhas são envolvidas com três aspas simples
variavel = '''
1       9
 2     8
  3   7       String multilinha
   4 6
    5
'''
# Mas não fica nada organizado. Melhor ir quebrando e usando \n.


# Documentação em funções 1


def dizer_ola():
    """Essa função mostra 'Olá' na tela"""
    print('Olá')


def saudar_convidado(nome):
    """Mostra uma mensagem de boas-vindas

    Essa função irá receber um nome como argumento
    Irá então inserir o nome dentro da função print
    E por fim mostrar na tela uma mensagem formatada
    """
    print(f'Como vai, {nome}? Estava ansioso por sua visita.')


# Documentação em funções 2


def somar(a, b):
    """
    Devolve a soma de a e b

    :param a: Primeiro número
    :type a: int or float
    :param b:Segundo número
    :type b: int or float

    :return: soma entra a e b
    :rtype: int or float
    """
    return a + b


def percorrer_iteravel(iteravel):
    """
    Percorre um valor iterável e imprime na tela
    :param iteravel: valor iterável
    :type iteravel: str or tuple or list or dict or generator

    :raise ValueError: Se o valor não for iterável
    """
    if not hasattr(iteravel, '__iter__'):
        raise ValueError('O valor passado não é iterável.')
    for valor in iteravel:
        print(valor)


# typehint - Não é necessariamente uma docstring, mas é uma funcionalidade que
# pode nos ajudar bastante. Serve para explicitarmos qual o tipo esperado de
# uma variável ou parâmetro e para dizer qual será o tipo de retorno de uma
# função


def descrever(nome: str, idade: int) -> str:
    # Após fechar parênteses nós colocamos uma seta pra indicar
    # o tipo de retorno
    return f'{nome} tem {idade} anos'


name: str = 'José'  # Assim deixamos explícito que o valor do nome é uma string
# name = 10 então se posteriormente tentarmos alterar o valor seremos alertados
# pelo IDE

# print(descrever(name, 'Pedro')) O mesmo acontece na chamada do método

# Esse if impede a linha de ser executada quando usamos help() em outro módulo
print(descrever(name, 57))


# Digamos que uma função pode retornar mais de um tipo de valor
# Ou que uma variável pode armazenar mais de um tipo
# Nesse caso precisamos importar Union em typing
from typing import Union


def subtrair(x, y) -> Union[int, float]:
    return x - y

# Gerenciadores de contexto nos permitem alocar e liberar recursos quando
# precisamos
# Basicamente isso é um gerenciador de contexto em Python
with open('aula_76_texto.txt', 'w', encoding='UTF-8') as file:
    file.write('Gerenciador de contexto padrão')
# Ele abre um arquivo no início do bloco e o fecha automaticamente no fim


# Criando um gerenciador de contexto personalizado
class Arquivo:

    def __init__(self, arquivo, modo, codificao='UTF-8'):
        self.arquivo = open(arquivo, modo, encoding=codificao)

    # Esse método é executado pelo with quando ele entra no gerenciador
    def __enter__(self):
        return self.arquivo

    # Esse método é executado quando o with encerra tudo
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Os demais parâmetros são preenchidos por informações de excessões
        # quando ocorre alguma dentro do with
        self.arquivo.close()
        return True  # Adicionando essa linha um erro nunca vai parar a execucao


# Basicamente estamos tratando a classe como um gerenciador
with Arquivo('aula_76_texto.txt', 'a+') as file:
    file.write('\nGerenciador de contexto com classe')
    # file.quwhquwijnk('nojn') Essa linha gera uma excessão


# Outra forma de criar um gerenciador de contexto

from contextlib import contextmanager
from time import sleep


@contextmanager
def abrir(arquivo, modo, codificacao='UTF-8'):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo, encoding=codificacao)
        yield arquivo  # Transforma a função em um gerador
    finally:
        print('Fechando arquivo')
        arquivo.close()   # Não chegaria aqui se fosse return ao invés de yield


with abrir('aula_76_texto.txt', 'a+') as file:
    file.write('\nGerenciador de contexto com contextmanager')
    sleep(3)

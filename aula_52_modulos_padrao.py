# Módulos padrão do Python
# Módulos são arquivos .py que podem ser importados e servem para
# expandir as funcionalidades da linguagem.

# Podemos importar um módulo inteiro
import sys
# Acessamos algo dentro dele usando nome_modulo.nome_funcionalidade
print(sys.platform)

# Podemos importar algo específico de um módulo
from math import pow
# Nesse caso podemos escrever diretamente apenas o nome da função
print(pow(5, 2))

# Podemos importar usando apelidos
import sys as sistema
# E chamamos o módulo pelo apelido
print(sistema.version)

# Também podemos apelidar função
from time import sleep as dormir
dormir(2)
print('zzzz...')

# Quando nós importamos apenas determinada função de um módulo há o risco de
# sobrescrever ela, por isso tenha cuidado com o nome que dá às suas funções
from random import randint

# Aqui está sendo executado o randint de random
print(randint(1, 5))


def randint(*args):
    # Aqui o randint já foi sobrescrito
    return 'Pato'


print(randint(1, 5))

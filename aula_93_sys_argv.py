# Executando arquivos com argumentos no sistema
# Para executar os programas .py como scripts

import sys

argumentos = sys.argv

# Quando executamos um arquivo python via terminal, tudo que é digitado depois
# fica armazenado em uma lista em sys.argv

# Por exemplo, em:
# python arquivo.py -b 12 queijo
# Teremos uma lista com ['arquivo.py', '-b', '12', 'queijo']
# Tudo é salvo na lista em formato string, a posição 0 SEMPRE vai ter o nome
# do próprio arquivo

# Sabendo disso, podemos criar scripts com python, para executar determinado
# comportamento de acordo com os argumentos recebidos

# Podemos parar o programa se nenhum argumento for passado:
if len(argumentos) == 1:
    print('Comandos disponíveis:')
    print('-o ---- Fala oi.')
    print('-t ---- Fala tchau.')
    sys.exit()

if '-o' in argumentos:
    print('Oi')
if '-t' in argumentos:
    print('Tchau')

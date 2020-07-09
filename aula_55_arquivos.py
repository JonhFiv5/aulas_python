# Criando, lendo, escrevendo e apagando arquivo

# Forma simples:
# Digitamos o nome do arquivo a ser criado/lido/alterado e em seguida a operação
file = open('aula_55_texto.txt', 'w+', encoding='UTF-8')
# Com write() adicionamos texto a ele
file.write('Requeijão com goiabada')
# Sempre que abrimos um arquivo precisamos lembrar de fechar depois
file.close()

# Entretanto pode ocorrer um erro nesse processo, poderíamos colocá-lo dentro de
# um bloco try, mas o python possui uma forma melhor de lidar com isso, que é
# usando o Gerenciador de contexto (context manager) with.
# Além de tratar as possíveis excessões que poderiam surgir o with também fecha
# o arquivo automaticamente

# Essa é a melhor forma de fazer isso em Python
with open('aula_55_texto.txt', 'r') as file:
    linha_1 = file.readline()
    print(linha_1)
    # Não precisamos fechar

# Se nós quisermos inserir conteúdo em um arquivo e querer ler ele antes de
# fechar precisamos redirecionar o ponteiro para o início do arquivo.
# Conforme vamos acrescentando linhas o ponteiro vai seguindo o fim da última
# linha, então para que nos seja retornado tod0 o conteúdo sem precisarmos
# reabrir, utilizamos a função seek, passando como argumento 0.
with open('aula_55_texto.txt', 'a+') as file:
    file.write('\nLinha 2')
    file.write('\nLinha 3')  # Aqui o ponteiro está após o 3
    file.seek(0)  # Isso devolve o ponteiro para o início do arquivo
    # Readlines nos devolve uma lista com todas as linhas após o ponteiro
    for linha in file.readlines():
        print(linha)

# Tipos de operações:
# 'r' -> Para leitura
# 'w' -> Para escrita, deleta tod0 o texto que havia anteriormente
# 'x' -> Exclusivo para a criação, falha se o arquivo existe
# 'a' -> Para escrita, concatena ao fim do texto já existente
#
# 'b' -> Modo binário
# 't' -> Modo texto (padrão)
# '+' -> Abre para update (escrita e leitura)

# Para deletar o arquivo basta usar o código abaixo
# import os
# os.remove('55_texto.txt')

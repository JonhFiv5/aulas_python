# Isso aqui é um módulo que está dentro de um pacote python
# Tod0 pacote python possui o arquivo __init__.py, isso serve para indicar que
# se trata de um pacote, mesmo que esse arquivo esteja vazio

# As funções criadas aqui foram importadas no arquivo 54_pacotes em aulas


def aumentar_preco(valor, porcentagem):
    return valor * (1 + porcentagem / 100)


def reduzir_preco(valor, porcentagem):
    return valor * (1 - porcentagem / 100)


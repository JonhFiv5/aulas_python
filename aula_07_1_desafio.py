# Criar variáveis para nome (str), idade (int),
# altura (float) e peso (float) de uma pessoa
# Criar variável com o ano atual (int)
# Obter o ano de nascimento da pessoa (baseadona idade e no ano atual)
# Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
# Exibir um texto com todos os valores na tela usando F-strings (com as chaves)

nome = 'Luís'
idade = 32
altura = 1.80
peso = 80.0
ano_atual = 2020
imc = peso / (altura ** 2)

print(
    f'{nome} tem {idade} anos, '
    f'{altura} de altura e pesa {peso}kg.\n'
    f'O IMC de {nome} é de {imc:.2f}.\n'
    f'{nome} nasceu em {ano_atual - idade}.'
)

# Crie uma função1 que recebe uma função2 como parâmetro e retorna o valor dessa
# função2 executada


def funcao_1(funcao):
    return funcao()


def funcao_2():
    return 'Função 2 executada'


print(funcao_1(funcao_2))

# _________________________________________________


def funcao_mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def funcao_oi(nome):
    return f'Oi {nome}'


def f_saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


resultado1 = funcao_mestre(funcao_oi, 'Pedro')
print(resultado1)

resultado2 = funcao_mestre(f_saudacao, 'César', saudacao='Bom dia')
print(resultado2)

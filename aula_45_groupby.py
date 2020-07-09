from itertools import groupby, tee

alunos = [
    {'Nome': 'Sérgio', 'Nota': 'A'},
    {'Nome': 'Pedro', 'Nota': 'B'},
    {'Nome': 'Ana', 'Nota': 'A'},
    {'Nome': 'Beatriz', 'Nota': 'C'},
    {'Nome': 'Marta', 'Nota': 'A'},
    {'Nome': 'Breno', 'Nota': 'C'},
    {'Nome': 'Heitor', 'Nota': 'B'},
    {'Nome': 'Diego', 'Nota': 'A'},
]

# Pra o groupby funcionar nossos dados precisam estar em ordem
# Vamos ordenar de acordo com a nota:
alunos.sort(key=lambda item: item['Nota'])

# Agora vamos agrupar eles de acordo com as notas
alunos_agrupados = groupby(alunos, key=lambda item: item['Nota'])

for agrupamento, grupo in alunos_agrupados:
    print(agrupamento)  # [0] -> Nota
    for aluno in grupo:  # [1] -> Iterador com os alunos
        print(aluno)
# A função groupby nos devolve tuplas de dois elementos, na posição 0 está o
# elemento da condição de agrupamento (título), nesse caso as notas (A, B, ou C)
# Na posição 1 está um iterador, com todos os elementos que fazem parte do grupo
# correspondente à nota.
print('-' * 40)
clientes = [
    ['Pedro', 'M'],
    ['Sônia', 'F'],
    ['Thiago', 'M'],
    ['Cleiton', 'M'],
    ['Roberta', 'F'],
    ['Mateus', 'M'],
    ['Maria', 'F'],
    ['Jorge', 'M'],
    ['Cláudia', 'F'],
]

agrupar_genero = lambda cliente: cliente[1]
clientes.sort(key=agrupar_genero)
clientes = groupby(clientes, key=agrupar_genero)
for sexo, grupo_cliente in clientes:
    # Na linha abaixo fazemos uma cópia do iterador, porque após percorrermos
    # ele fica vazio, então não poderíamos pegar a quantidade de clientes
    grupo_1, grupo_2 = tee(grupo_cliente)
    print(f'{len(list(grupo_1))} clientes são do sexo {sexo}.')
    for cliente in grupo_2:
        print(f'\t{cliente}')

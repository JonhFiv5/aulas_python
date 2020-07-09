# Dicionários são escritos entre chaves{}, a principal diferença entre
# eles e listas é que enquanto listas geram números automaticamente como índices
# em dicionários nós criamos nossos próprios índices, eles podem ser nomeados
# com as mesmas regras de nomenclatura usadas para variáveis
# Dicionários armazenam itens em pares chave-valor

exemplo_dicio = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3',
}
print(exemplo_dicio['chave1'])

# Adicionar um novo par chave-valor:
exemplo_dicio['chave4'] = 'valor4'
print(exemplo_dicio)

# Remover um par
del exemplo_dicio['chave2']
print(exemplo_dicio)

# Outra forma de criar um dicionário
exemplo_dicio = dict(chave_a='Abelha', chave_b='Búfalo', chave_c='Cobra')
print(exemplo_dicio)

# Também podemos buscar o valor de uma chave através da função get, dessa forma
# é retornado num None ao invés de uma excessão caso a chave não exista.

# Percorrendo dicionários com um laço
dicio_laco = {'nome': 'João Kaíque', 'Sobrenome': 'O. Aguiar', 'idade': 20}
# Percorrendo chave e valor
for chave, valor in dicio_laco.items():
    print(chave, valor)

# Percorrendo as chaves
for chave in dicio_laco:  # Ou for chave in dicio_laco.keys()
    pass
    # print(dicio_laco[chave])

# Percorrendo os valores
for valor in dicio_laco.values():
    pass
    # print(valor_i)

# Para fazer uma cópia real de um dicionário e fazer alterações em um sem
# alterar o outro é preciso fazer uma 'cópia profunda', através do módulo copy:
# import copy
# copia_dicio = copy.deepcopy(original_dicio)
# Se ao invés disso usarmos a função copy() do próprio dicionário estaremos
# Criando uma cópia rasa, ou seja, se dentro do dicionário houver elementos
# mutáveis como listas ou outros dicionários, alterações realizadas nesses
# elementos irão afetar os dois dicionários, tanto o original quanto a cópia

# É possível converter uma lista ou tupla em dicionário através de dict(lista)
# caso ela tenha uma estrutura semelhante a essa:
lista = [
    ['chave1', 'valor1'],
    ['chave2', 'valor2']
]

dicio_lista = dict(lista)
print(dicio_lista)

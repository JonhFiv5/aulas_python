# A função map serve para percorrer uma lista fazendo modificações em todos
# (ou nem todos) os seus elementos
from copy import deepcopy

lista_numero = [2, 3, 4, 5, 6, 7]

# Nesse map vamos multiplicar os números ímpares por 2 e não alterar os pares
lista_pares = map(  # Recebe dois argumentos
    lambda numero:  # 1. Uma função que vai alterar os elementos da lista
    numero if numero % 2 == 0
    else numero * 2,
    lista_numero  # 2. Uma lista
)
# A função map nos devolve um iterador (map object), então precisamos converter
lista_pares = list(lista_pares)
print(lista_numero)
print(lista_pares)

# Nós não precisamos alterar todos os valores que entram no map, como você viu,
# mas o map sempre vai retornar o mesmo número de valores que recebeu. Então se
# um item não for modificado é obrigatório retornar no mínimo o item original.
# (É isso que foi feito na função lambda)

produtos = [
    {'nome': 'Caneta', 'Preco': 0.75},
    {'nome': 'Lápis', 'Preco': 1.10},
    {'nome': 'Caderno', 'Preco': 14.50},
    {'nome': 'Mochila', 'Preco': 67},
    {'nome': 'Batata', 'Preco': 2.25},
]

# Adicionar 5% ao preço dos produtos


def aumentar_preco(produto):
    prod_copia = deepcopy(produto)  # Precisamos fazer uma cópia para não
    # alterar também o dicionário original (se não quisermos alterar ele, claro)
    prod_copia['Preco'] = round(prod_copia['Preco'] * 1.05, 2)
    return prod_copia


produtos_aumento = map(aumentar_preco, produtos)  # É aceita qualquer função
# não só lambda. E é passada para ele o argumento automaticamente

produtos_aumento = list(produtos_aumento)

print('\nDicionário original')
for pd in produtos:
    print(pd)

print('\nDicionário após o map')
for pd in produtos_aumento:
    print(pd)

# Listas em Python
# fatiamento
# append, insert, pop, del, clear, extend, +
# min, max
# range

# Listas são um tipo de dado que podem armazenar diversos valores.
# Uma lista suporta armazenar vários tipos de dados simultâneamente, mas o ideal
# é criar listas homogêneas, com um único tipo.
# Acessamos os valores em uma lista através dos índices, que iniciam em 0.
lista_heterogenea = ['Oi', 15, True, 10.22]
lista_homogenea = ['a', 'b', 'c', 'd']
print(f'Lista heterogênea: {lista_heterogenea}')
print(f'Lista homogênea: {lista_homogenea}')


# Fatiamento
lista_completa = [1, 2, 3, 4, 5, 6]
lista_fatiada = lista_completa[0:3]  # O elemento do índice não é incluído
print(lista_completa)
print(lista_fatiada)

# Se atribuirmos uma lista para outra elas ainda estarão 'amarradas', apontam
# para o mesmo endereço da memória, então alterações em uma afetará a outra
lista_original = ['queijo', 'goiaba', 'sabão']
lista_copia = lista_original
lista_copia[0] = 'presunto'
print(lista_original, lista_copia)
# Para realizarmos uma cópia da lista, e cada uma apontar para seu próprio local
# da memória podemos realizar o fatiamento da lista inteira
lista_original_02 = [1, 2, 3]
lista_copia_02 = lista_original_02[:]  # Fatiamento da lista inteira
lista_copia_02[0] = 100
print(lista_original_02, lista_copia_02)

# Junção de listas
# Em uma nova lista(+):
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)
# Em uma lista existente(extend):
lista_01 = ['a', 'b', 'c']
lista_02 = ['d', 'e', 'f']
lista_01.extend(lista_02)
print(lista_01)

# A função append adiciona um novo elemento no fim da lista
li = ['biscoito']
li.append('Bolacha')
li.append(15)
print(li)

# A função insert adiciona um nova elemento na lista, onde desejarmos
lis = [1, 2, 3, 4, 5]
lis.insert(2, 'batata')
print(lis)

# A função pop por padrão vai remover o último elemento da lista
# Podemos guardar esse elemento se atribuirmos a operação a alguma variável
lista = ['oi', 'bye', 'olá', 'tchau']
item_removido_1 = lista.pop()  # Vai remover o último se não tiver argumentos
print(lista, item_removido_1)
item_removido_2 = lista.pop(1)  # Também podemos passar o índice que queremos
print(lista, item_removido_2)

# Criando rapidamente uma lista de números
# Neste exemplo precisamos usar o asterisco para o Python desempacotar o
# objeto iterável range
# Listas, strings e a função range são iteráveis, podemos percorrer com um laço
# numeros_pares = [*range(2, 101, 2)]
numeros_pares = list(range(2, 101, 2))  # A função list também funciona
print(numeros_pares)

# A função del vai excluir o que passarmos para ele. Pode ser um índice de uma
# lista ou uma fatia dela, por exemplo.
numeros_impares = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del(numeros_impares[::2])  # Fatia dos números pares
print(numeros_impares)

# Função max retorna o maior valor e min o menor
sequencia_numerica = [-19, 45, 12, -3, 75]
print(f'Maior: {max(sequencia_numerica)}')
print(f'Menor: {min(sequencia_numerica)}')


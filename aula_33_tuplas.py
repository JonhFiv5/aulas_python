# Tuplas são como listas, mas são imutáveis. Seus elementos são colocados
# entre parênteses
t1 = ('a', 'Queijo', 23)
print(f't1 = {t1}')

# Se atribuirmos também uma sequência de elementos sem parênteses será criada
# uma tupla
t2 = 1, 2, 3, 'pipoca'
print(f't1 = {type(t1)} t2 = {type(t2)}')

# Para criarmos tuplas com apenas um elemento é preciso adicionar uma vírgula
# após ele
t3 = ('b',)
t4 = 5,
print(f't3 = {type(t3)} t4 = {type(t4)}')

# Podemos multiplicar tuplas, fazendo cópias dos seus elementos
t5 = ('início', 'meio', 'fim') * 3
# t5 *= 3
print(t5)

# Também podemos transformar tuplas em lista:
t6 = ('pipoca', 'manteiga', 'açúcar')
lista_cinema = list(t6)
print(f'lista_cinema = {lista_cinema} {type(lista_cinema)}')
# Convertendo de volta...
# tupla_cinema = tuple(lista_cinema)


def editar_tupla(tupla, indice, novo_elemento=None, delete=False):
    lista = list(tupla)
    if delete:
        del lista[indice]
    else:
        lista[indice] = novo_elemento
    tupla = tuple(lista)
    return tupla


tupla_teste = (1, 2, 3, 'me tira daqui', 5)

tupla_teste = editar_tupla(tupla_teste, 3, delete=True)  # Remove um índice
print(tupla_teste)

tupla_teste = editar_tupla(tupla_teste, 0, 'Cleiton')  # Altera valor
print(tupla_teste)

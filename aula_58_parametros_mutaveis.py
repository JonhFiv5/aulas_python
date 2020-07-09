# Problema dos parâmetros mutáveis em funções
# Mutáveis: Dicionários, listas, etc
# Imutáveis: Strings, tuplas, números, booleanos, None...

# Na função abaixo o parâmetro lista é mutável


def lista_clientes(clientes, lista=[]):
    lista.extend(clientes)
    return lista


clientes1 = lista_clientes(['Ana', 'Roberto', 'Pedro'])
clientes2 = lista_clientes(['Zé', 'Tiago', 'Augusto'])
print(clientes1)
print(clientes2)
# Repare que as duas listas deveriam estar separadas, mas estão juntas em uma só
# Esse problema ocorreu porque o argumento lista da função é mutável.
# Aquela lista foi criada uma única vez, então sempre que executamos a função
# é feito um append na mesma lista. Então tanto clientes1 quanto clientes2
# referenciam para o mesmo espaço da memória.

# Para resolver esse problema NÃO devemos utilizar parâmetros mutáveis,
# ao invés disso podemos utilizar um parâmetro imutável e dentro da função
# atribuir a ele um objeto mutável. Assim sempre que a função for chamada é
# criado um novo objeto


def lista_compras(produtos, lista=None):
    if lista is None:
        lista = []
    print(id(lista))
    lista.extend(produtos)
    return lista


compras1 = lista_compras(['Queijo', 'Abacate', 'Benegripe'])
compras2 = lista_compras(['Bolo', 'Alface', 'Frango'])

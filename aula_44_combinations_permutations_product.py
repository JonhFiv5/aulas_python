from itertools import combinations, permutations, product

# Combinations, permutations e product - itertools
# Combinação - Ordem não importa
# Permutação - Ordem importa
# Ambos não repetem valores únicos
# Produto (arranjo com repetição) - Ordem importa e repete valores únicos

# É aquele assunto de matemática, considere para esse exemplo os número 1, 2 e 3

# A combinação não vai aceitar grupos iguais com elementos em ordens diferentes
# Combinação de 2: 1-2, 1-3, 2-3
# A permutação aceita grupos com os mesmos elementos em ordens diferentes
# Permutação de 2: 1-2, 2-1, 1-3, 3-1, 2-3, 3-2
# O produto vai aceitar grupos com os mesmos elementos, em ordens
# diferentes e com repetição de elementos:
# Produto de 2: 1-1, 1-2, 2-1, 2-2, 1-3, 3-1, 3-3, etc...

cores = ['Azul', 'Vermelho', 'Preto']
# Nós passamos o iterável e o tamanho dos grupos que queremos que sejam formados
combinacao_cores = list(combinations(cores, 2))
# Em permutação o tamanho é opcional, se não passarmos vai ser igual à
# quantidade de elementos
permutacao_cores = list(permutations(cores, 2))
# Em produto nós passamos o tamanho dos grupos no argumento repeat, já que ele
# forma grupos com elementos repetidos
produto_cores = list(product(cores, repeat=2))

print('Combinação -', cores, '-' * 30)
for grupo in combinacao_cores:
    print(grupo)

print('\nPermutação -', cores, '-' * 30)
for grupo in permutacao_cores:
    print(grupo)

print('\nProduto -', cores, '-' * 30)
for grupo in produto_cores:
    print(grupo)

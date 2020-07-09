# Sets são como listas, mas só admitem valores únicos
# Nós criamos sets entre chaves, assim como dicionários, mas eles não possuem
# chave

# Colocamos valores repetidos (1, 2)
s1 = {1, 2, 3, 'a', 'b', 1, 2}
# Esses valores não são salvos, o set descarta repetições automaticamente,
# guardando apenas um valor de cada
print(s1)
# Não podemos pegar um valor armazenado em set através de índice s1[0]
# Mas podemos pegar através de um laço for

# Criar um set vazio
s2 = set()
# Adicionar um valor
s2.add('Paçoca')
s2.add('Vitória')
# Remover um valor
s2.discard('Paçoca')

# A função update também adiciona elementos em um set, mas se o elemento for
# iterável, ele irá desempacotar ele antes de adicionar ao set. Por exemplo, se
# passarmos uma string ele vai dividir as letras
# Outra coisa importante sobre sets é que ele não se preocupa com a ordem
# dos elementos, por isso não podemos acessá-los com índice. Cada vez que é
# exibido pode estar em uma ordem diferente
palavra_decomposta = set()
palavra_decomposta.update('Supermercado')
print(palavra_decomposta)

# União de sets (junção de todos os elementos)
# função union ou o sinal |
s_a = {1, 2, 3, 8}
s_b = {1, 2, 3, 4, 5}

s_uniao = s_a | s_b
print('União:', s_uniao)

# Intersecção (elementos em comum)
# função intersection ou o sinal $
s_inter = s_a & s_b
print('Intersecção:', s_inter)

# Diferença (elementos existentes apenas no set da esquerda (s_a)
# função difference ou o sinal -
s_dif = s_a - s_b
print('Diferença:', s_dif)

s_dif = s_b - s_a
print('Diferença:', s_dif)

# Diferença simétrica (elementos únicos de cada set)
# função symmetric_difference ou o sinal ^
s_simet = s_a ^ s_b
print('Diferença simétrica:', s_simet)

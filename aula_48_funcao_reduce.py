# A função filter é uma acumuladora, ela vai percorrer um iterável sempre
# passando para a função dois valores, o valor acumulado e o valor atual. Vai
# fazer isso para cada índice e no fim devolve apenas o valor acumulado
# Essa função precisa ser importada antes de ser usada
from functools import reduce

# Diferente de map e filter, reduce nos devolve apenas o dado, e não um iterador
lista_numeros = [1, 2, 3]
soma = reduce(lambda acumulado, atual: acumulado + atual, lista_numeros)
# print(soma)

batata = 'Batata'
lista_letras = [letra for letra in batata]
palavra = reduce(lambda acumulado, atual: acumulado + atual, lista_letras)
print(palavra)

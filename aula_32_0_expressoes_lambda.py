# Espressões lambda, também chamadas de funções anônimas
# Uma função normal:


def somar(num1, num2):
    return num1 + num2


print(somar(4, 5))

# A mesma função que a de cima, mas escrita na forma de função anônima:
# Escrevemos 'lambda', os argumentos, dois pontos, o retorno
# Observe que é semelhante a arrow functions de js, mas os argumentos não têm ()

variavel_soma = lambda num1, num2: num1 + num2
print(variavel_soma(5, 5))

# Nota: Embora possamos atribuir uma expressão lambda para uma variável, a PEP-8
# reclama disso, dizendo que é recomendado utilizar def.
# A melhor forma de usar lambda é quando não precisamos ter uma função que
# usaremos mais vezes, mas sim quando passamos uma função como argumentos para
# outra.

# Exemplo, ordenar uma lista de acordo com o preço

lista = [
    ['preco5', 8],
    ['preco1', 13],
    ['preco2', 6],
    ['preco4', 50],
    ['preco3', 7],
]
# Se usarmos apenas o sort ele irá ordenar apenas de acordo com o índice 0 de
# cada lista, 'precox'.
lista.sort()
print('-' * 70)
print('Lista alterada diretamente com sort(), sem lambda. Ela foi ordenada de\n'
      'acordo com o índice 0 de cada item.')
print(lista)
print('-' * 70)
# Precisamos indicar que queremos ordenar de acordo com o índice 1, o valor do
# preço. Para isso a função sort recebe uma callback, que recebe cada elementos
# da nossa lista, ou seja, cada uma das listas contidas dentro dela. Então
# podemos passar como parâmetro uma função lambda, que recebe cada lista e
# devolve o índice 1 delas. Assim o sort irá ordenar os preços:
# ! em sort passamos a lambda com o argumento nomeado 'key'
lista.sort(key=lambda item: item[1])
print('Lista alterada com sort(). Preços em ordem crescente com lambda:')
print(lista)
print('-' * 70)

# A função sort() vai alterar a lista original, para alterar apenas em um
# determinado momento podemos uma a função sorted. Que recebe como parâmetros
# a lista, uma função 'key' e o argumento reverse (assim como sort)
print('Lista alterada com sorted(). Preços em ordem descrescente com lambda:')
print(sorted(lista, key=lambda item: item[1], reverse=True))
print('-' * 70)
# Ordenou em ordem decrescente, mas foi alterado apenas nessa linha, a lista
# continua como antes:
print('A lista foi modificada em sua raíz apenas pelo sort():')
print(lista)

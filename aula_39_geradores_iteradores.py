import sys  # Veja linha 31
# Geradores, iteradores e iteráveis
# Listas, tuplas, dicionários, strings, sets... Todos são iteráveis
# Para saber se determinado dado é iterável usamos a função hasattr()
# Passando o objeto e entre aspas o tipo de atributo (__iter__ - iterável)
print('Iteráveis', '-' * 20)
print('String ', hasattr('João', '__iter__'))
print('Lista ', hasattr([], '__iter__'))
print('Dicionário ', hasattr({}, '__iter__'))
print('range() ', hasattr(range(1), '__iter__'))
# Números não são iteráveis
print('Número ', hasattr(2020, '__iter__'))

# Para saber se determinado dado é um iterador, verificamos se ele possui o
# atributo __next__
print('Iteradores', '-' * 20)
print('Lista ', hasattr([], '__next__'))
# Um iterável não é nativamente um iterador, mas pode ser transformado
# utilizando a função iter(). Iteradores são elementos que possuem a
# função next(), isso significa que toda vez que chamarmos esse elemento
# dessa forma será devolvido o próximo valor que está armazenado.
# Iteradores também são iteráveis, podemos percorrer seus elementos com laços,
# mas não podemos acessar seus valores através de índices.
lista = ['a', 'b', 'c']
lista = iter(lista)
print(next(lista))  # a
print(next(lista))  # b
print(next(lista))  # c
# print(next(lista)) Só há três elementos na lista, então aqui daria erro
for a in lista:
    print('Neste ponto a lista já está vazia, por causa dos três next().')

print('Geradores', '-' * 20)
# A diferença entre geradores e iteráveis como listas é bem simples, uma lista
# vai armazenar todos os valores de uma vez, ocupando MUITO mais espaço na
# memória. Um gerador, por sua vez, armazena apenas um número por vez

# Criando uma lista comum usando list comprehension
lista2 = [x for x in range(10000)]  # Lista com dez mil números
print(sys.getsizeof(lista2), 'bytes')

# Nós podemos facilmente criar um gerador utilizando o código acima, basta
# apenas substituir as chaves [] por parênteses ()
lista3 = (x for x in range(10000))  # Gerador com dez mil números
print(sys.getsizeof(lista3), 'bytes')
# Geradores também são iteráveis e iteradores
print(hasattr(lista3, '__iter__'))
print(hasattr(lista3, '__next__'))

# Também podemos criar um gerador com o declarador yield
# Função geradora com yield:


def gera():
    for n in range(10000):
        yield n


lista4 = gera()  # A partir daqui lista4 recebe um gerador de 0 a 9999
print(sys.getsizeof(lista4))

# Um gerador é iterável com laços
for i in lista4:
    print('Gerado:', i)
    if i == 10:
        break

# O next também funciona
print(next(lista4))

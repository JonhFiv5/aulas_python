# Um laço for converte um iterável para um iterador em tempo de execução
# Ou seja, enquanto o laço está sendo executado uma lista, por exemplo, é
# convertida em iterador e é aplicado sobre ela um next() a cada volta do laço
# até que o iterador seja esgotado ou o laço interrompido, após isso a nossa
# lista volta a ser o mesmo iterável que era antes

import sys

lista = [1, 2, 3, 4]
print(type(lista))
print(lista)

for i in lista:
    pass
    # print(i)

# Esse for faz mais ou menos o seguinte:
iterador_lista = iter(lista)
print(type(iterador_lista))
print(next(iterador_lista))  # 1
print(next(iterador_lista))  # 2
print(next(iterador_lista))  # 3
print(next(iterador_lista))  # 4
# Nesse ponto o iterador foi totalmente utilizado, está vazio
for i in iterador_lista:
    print('Valor no iterador')

gerador_lista = (x for x in lista)
# print(type(gerador_lista))
# print(next(gerador_lista))
# print(next(gerador_lista))
# print(next(gerador_lista))
# print(next(gerador_lista))

# Assim como o iterador, o gerador está vazio nesse ponto, devido ao next()
for i in gerador_lista:
    print('Valor no gerador')

# Mesmo que tenhamos usado o next(), se tivesse sido um laço, o iterador ou
# gerador também estaria vazio após a execução. Iteradores e geradores são
# esvaziados depois que seus valores são usados.

# Todos os geradores são iteradores, mas nem todos iteradores são geradores
# Cada um tem suas vantagens e desvantagens, pesquise mais sobre o assunto

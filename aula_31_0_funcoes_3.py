# Trabalhando com um número indefinido de argumentos
# *args (arguments) usando um asterisco indicamos que a função pode receber
# vários argumentos. Esses argumentos ficam salvos em uma tupla.


def soma_tudo(*numeros):
    # Podemos usar a palavra que quisermos, mas por convenção é usado args
    print(type(numeros))
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_tudo(5, 5, 5, 10, 5))

# Se nós passarmos uma lista para um *args ela ficará no índice 0 da tupla args,
# assim para acessar cada elemento da lista precisariamos usar:
# args[0][0], args[0][1], args[0][2], etc... Para facilitar isso poderíamos
# desempacotar a lista no momento em que a enviamos para a função, com o
# caracter desempacotador asterisco, assim cada item da lista ficaria em uma
# posição diferente dentro da tupla, como itens separados.

lista_numeros = [2, 3, 4, 5]
print(soma_tudo(*lista_numeros))

# **kargs (keyword arguments) com o uso de dois asteriscos podemos passar um
# número indeterminado de argumentos nomeados, eles ficarão salvos dentro de um
# dicionário


def nomeados(**kwargs):
    for chaves in kwargs.keys():
        print(f'{chaves}: {kwargs[chaves]}')


nomeados(nome='Kleiton', sobrenome='Jeff', idade=48)

# Nota sobre dicionários: nós podemos pegar um valor usando diretamente
# dicio['chave']. Entretanto isso pode gerar um erro quando não tivermos certeza
# se aquela chave existe no dicionário, é o que acontece ao usarmos **kwargs.
# Por isso, outra forma mais segura seria dicio.get('chave'), pois essa função
# não dará erro, apenas retornará None se a chave não existir

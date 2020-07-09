# Compreensão de listas, é basicamente uma forma rápida para lidar conjuntamente
# com os elementos de uma lista utilizando menos linhas de código
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# No código abaixo nós criamos uma nova lista percorrendo todos os elementos
# da lista orginando e alterando eles, multiplicando cada um por dois.
# A sintaxe: (modificação) for (elemento) in (lista)
# É semelhante a um laço for, a diferença é só isso de adicionar no início qual
# a modificação a ser feita.
exemplo_1 = [valor * 2 for valor in lista]
print(f'{lista}\n{exemplo_1}\n{"-" * 70}')

# Transformando os elementos em string
exemplo_2 = [str(valor) for valor in lista]
print(f'{lista}\n{exemplo_2}\n{"-" * 70}')

# Podemos incluir mais de um laço, o segundo irá ser executado para cada
# elemento da lista.
# Criar três coordenadas pra cada elemento (0, 1, 2)
exemplo_3 = [[v1, v2] for v1 in lista for v2 in range(0, 3)]
print(f'{lista}\n{exemplo_3}\n{"-" * 70}')

# Também podemos trabalhar diretamente em cima de elementos iteráveis, não
# necessariamente apenas listas
letras_maiusculas = [letra.upper() for letra in 'Papagaio']
print(f'{letras_maiusculas}\n{"-" * 70}')

# Filtrando valores, colocamos a condição no fim
lista_0a100 = list(range(0, 101))

multiplos_3_5 = [
    valor for valor in lista_0a100
    if valor % 3 == 0
    if valor % 5 == 0  # També poderia ser and ao invés de if
]
print(multiplos_3_5)

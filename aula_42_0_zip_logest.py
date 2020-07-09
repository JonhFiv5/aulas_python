# Zip - Unindo iteráveis
# Zip_logest - Itertools

from itertools import zip_longest

# O zip funciona unindo iteráveis, no exemplo das listas, ele vai unir o índice
# 0 da primeira lista com o 0 da segunda em tuplas, e assim sucessivamente com
# os demais elementos da lista até todos estarem agrupados.
# Dentro da função zip() podemos passar mais de dois iteráveis, nesse caso cada
# tupla vai ter o tamanho da quantidade de iteráveis passada, já que pega um
# elemento de cada.
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio Branco']
estados = ['SP', 'MG', 'BA']

cidade_estado = zip(cidades, estados)
cidade_estado = list(cidade_estado)
print(cidade_estado)

# Observe que no exemplo anterior há quatro cidade e três estados, a função zip
# Só irá considerar então três grupos de tuplas, descartando assim a quarta
# cidade, já que não há um elemento pra combinar com ela na outra lista.

# Para unirmos iteráveis de tamanho diferente há a função zip_logest, que deve
# ser importada do módulo itertools
cidade_estado_2 = zip_longest(cidades, estados, fillvalue='Vazio')
# No parâmetro fillvalue nós escrevemos um valor padrão, que será passado
# como par para todos aqueles elementos que não tiverem um, no caso a cidade
# Rio Branco. Se não usarmos esse parâmetro será passado None
print(list(cidade_estado_2))

# Desempacotamento de listas em Python

# Uma forma de desempacotamento
# (A quantidade de variáveis precisa ser igual a de valores)
lista = ['Valor1', 'Valor2', 'Valor3']
var1, var2, var3 = lista
print(var1)
print(var2)
print(var3)

# (Podemos usar fatiamento)
var1, var2 = lista[0:-1]  # Não vai contar o último (retorna 2 valores)
print(var1)
print(var2)

# Ou usar um (*), para criar outra lista com os elementos restantes
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
letra_a, letra_b, letra_c, *demais_letras = letras
print(letra_a)
print(letra_b)
print(letra_c)
print(demais_letras)
# Se adicionarmos mais variáveis após *demais_letras elas receberiam os
# últimos valores da lista em ordem, assim:
letra_a, letra_b, *letras_centrais, penultima, ultima = letras
print(letras_centrais)
print(penultima)  # 'h'
print(ultima)  # 'i'

# Ou então...
*primeiras_letras, ultima_letra = letras
print(primeiras_letras)
print(ultima_letra)

# Se nós quisermos indicar para outras pessoas que os demais valores não vão ser
# usados utilizamos o underscore como nome da lista, assim: *_

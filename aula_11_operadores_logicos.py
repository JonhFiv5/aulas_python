# São usados entre dois ou mais valores booleanos (comparações)

var_a = 1
var_b = 1
var_c = 2

condicao_verdadeira = var_a < var_c
condicao_falsa = var_a > var_b

# or - Retorna True caso alguma condição seja True
print(condicao_verdadeira or condicao_falsa)

# and - Retorna True caso ambas as condições sejam True
print(condicao_verdadeira and condicao_verdadeira)

# not (!) - Inverte o valor lógico de uma condição
print(not condicao_verdadeira)

# in - Retorna True se um valor estiver contido em outro
print('nana' in 'banana')

# not in - Retorna True se um valor não estiver contido em outro
print(12 not in [1, 2, 3, 4, 5])

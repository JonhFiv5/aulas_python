# Formatando valores com modificadores (vale com format() e F-strings)

# :s - string
# :d - integer
# :f - float
# :.(numero_casas_decimais)f - Determina quantas casas decimais mostrar
# :(caractere)(> ou < ou ^) - (Quantidade) (Tipo - s, d ou f)

# > - Esquerda
# < - Direita
# ^ - Centro

# num_1 = 10
# num_2 = 3
# divisao = num_1 / num_2

# print(divisao)  # Sem formatação
# print(f'{divisao:.2f}')  # Formatação com F-strings
# print('{:.2f}'.format(divisao))  # Formatação com format()

nome = 'João'
# A próxima linha significa que o tamanho total do nome será de 30 caracteres
# que o nome ficará centralizado (^), e que os espaços restantes para concluir
# 30 serão preenchidos por hífen (-). Por último deixamos explícito que é string
# (s), isso é opcional.
print(f'{nome:-^30s}')
print(f'{nome:8^30}')

# Exemplos pra deixar mais claro
print(f'{25:0<6}')
print(f'{25:0>6}')
print(f'{25:0^6}')

# Funções string que funcionam de forma semelhante (ljust, rjust, center)
# (tamanho_total, caracter_preenchimento)
print('Esquerda'.ljust(14, '_'))
print('Direita'.rjust(14, '_'))
print('Centro'.center(14, '_'))

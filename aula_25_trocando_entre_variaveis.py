# Trocar valores entre variáveis
# Em outras linguagens, para trocar valores entre duas variáveis precisamos de
# uma terceira, assim:

nome_1 = 'Augusto'
nome_2 = 'Martha'

nome_temp = nome_1
nome_1 = nome_2
nome_2 = nome_temp

print(f'nome_1 = {nome_1} nome_2 = {nome_2}')

# Já em Python temos uma forma mais fácil de fazer isso:
fruta_1 = 'Maçã'
fruta_2 = 'Goiaba'

fruta_1, fruta_2 = fruta_2, fruta_1  # Pode ser feito com mais de duas variáveis

print(f'fruta_1 = {fruta_1} fruta_2 = {fruta_2}')

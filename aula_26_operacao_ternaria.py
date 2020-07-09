# Operador ternário
# É uma forma bem reduzida da estrutura if-else, é feito é uma única linha

nome = str(input('Digite seu nome: '))

# Exemplo sem operador ternário
if nome.lower() == 'joão kaíque':
    print('Bem-vindo!')
else:
    print('Adeus.')

# utilizando operador ternário
print('Bem-vindo!') if nome.lower() == 'joão kaíque' else print('Adeus.')

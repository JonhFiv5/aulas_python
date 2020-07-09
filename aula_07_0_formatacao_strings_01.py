nome = 'Pedrim'
idade = 34
peso = 77
altura = 1.73
imc = peso / (altura ** 2)

# Sem formatação
print('Eu sou', nome, 'tenho', idade, 'anos e meu IMC é', imc)

# Utilizando F-strings
print(f'Eu sou {nome} tenho {idade} anos e meu IMC é {imc:.2f}')

# Utilizando a função format, é preciso observar a ordem das chaves
print('Eu sou {} tenho {} anos e meu IMC é {:.2f}'.format(nome, idade, imc))

# Macetes com format (com eles não precisamos nos preocupar com a ordem)
# Passando o índice dos valores nas chaves, podemos reuzar eles onde desejarmos
print('{2} {0} {1} {2} {3}'.format('a', 'b', 'c', 'd', 'e'))

# Também podemos usar parâmetros nomeados
print('{a} {b} {c} {a}'.format(a='<------->', b='Batata', c='Paçoca'))

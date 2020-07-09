# Podemos receber dados do teclado pela função input()
nome = input('Qual é o seu nome? ')
print(f'Olá {nome}!')

# Por padrão input() retorna string, por isso podemos precisar de casting
numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite outro número: '))
print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')

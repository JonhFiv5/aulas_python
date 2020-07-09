# For in em Python
# Iterando strings com for
# Função range(start=0, stop, step=1)

texto = 'Abacate é doce'

# O for in não necessita de um contador
for letra in texto:
    print(letra)
print('-' * 10)

# Caso precisemos de um contador, podemos utilizar a função enumerate.
# Ela numera cada iteração.
for indice, letra in enumerate(texto):
    print(f'{letra}[{indice}]')
print('-' * 10)

# Também podemos criar um for com contador usando a função range
# o range recebe a posição inicial, a posição final e o passo
# Por padrão, posição inicial é 0 e o passo é 1. Então podemos omitir essas
# informações e digitar somente o valor da posição final.
# range(0, 10, 1) == range(10)
for contador in range(len(texto)):
    print(f'{texto[contador]}[{contador}]')
print('-' * 10)

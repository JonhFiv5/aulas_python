# While  / Else
# Contadores
# Acumuladores

contador = 0  # É incrementado linearmente a cada repetição
acumulador = 0  # Acumula valores. Não é necessariamente linear
while contador <= 5:
    print(contador)
    contador += 1
    acumulador += contador
print(acumulador)

# Em Python, podemos usar else após um while. Esse bloco else será executado
# no momento em que a condição do while der False e o loop chegar ao fim.
# Esse else pode ser útil em blocos onde o break pode ou não ser executado.
# Se o break ocorrer, então o loop para antes da condição ser falsa, então o
# else não é executado.

entrada = 0
while entrada != 's':
    entrada = input('Digite [s] para sair: ')
    if entrada == 'cleber':
        break
else:
    print('Não sou executado se o loop for interrompido.')
print('Eu sou executado de qualquer jeito.')

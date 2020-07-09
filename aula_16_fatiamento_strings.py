# Fatiamento de strings [inicio:fim:passo]
# Nota -1 indica a última posição, -2 a penúltima e assim sucessivamente

# início 0, fim vazio e passo 1 = imprime tudo
print('Banana'[0::1])
# início -1, fim vazio e passo -1 = imprime ao contrário
print('Pedro'[-1::-1])

# A última posição é sempre ignorada, para uma posição antes
# Assim se imprimirmos de 0 até 4, vai mostrar até o index 3
print('Lucas'[0:4:1])

# Mesmo se não indicar nada o passo padrão é 1
print('Canela'[0::])
print('Canela'[0::2])

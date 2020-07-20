import random
import string

# Gera um inteiro aleatório entre dois números
inteiro_rd = random.randint(0, 10)

# Gera um inteiro aleatório usando a funcionalidade de range
inteiro_par = random.randrange(0, 100, 2)

# Gera um flutuante aleatório entre dois números
flutuante_un = random.uniform(15, 20)

# Gera um flutuante aleatório entre 0 e 1
flutuante_rd = random.random()


lista = ['Azul', 'Vermelho', 'Amarelo', 'Verde', 'Preto']
# Seleciona aleatoriamente um valor em uma lista
resultado_rd = random.choice(lista)

# Seleciona aleatoriamente quantos valores quisermos em uma lista
resultado_rds = random.choices(lista, k=3)
# Mas podemos ter valores repetidos, para ter valores únicos é só usar:
# random.sample(lista, k=3)

# Embaralha uma lista
random.shuffle(lista)
print(lista)

# Gerando uma senha aleatória
letras = string.ascii_letters
numeros = string.digits
l_n = letras + numeros
senha = ''.join(random.choices(l_n, k=10))
print(senha)

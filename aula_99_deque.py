# Trabalhando com LIFO e FIFO

# LIFO -> Last in, first out (Pilha/Stack)
# FIFO -> First in, first out (Fila/Queue)

# collections possuem estruturas de dados de alto desempenho
from collections import deque

# Pilha de livros

livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')

print(livros)
livro_removido = livros.pop()
print(livros)
# O último livro a entrar é o primeiro a sair através do método pop()
print(livro_removido)


# No caso de uma fila, teríamos que remover o primeiro elemento de uma lista
# para que o primeiro a entrar seja o primeiro a sair
# Entretanto fazer um pop no início da fila é mais pesado, já que vai mudar o
# o índice de todos os demais elementos
# Há uma forma otimizada de fazer um pop assim, é utilizando o módulo deque

# Precisamos transformar uma lista comum em deque
fila_banco = deque()
fila_banco.append('Cleiton')
fila_banco.append('Luna')
fila_banco.append('Samuel')
fila_banco.append('Jorge')

cliente_atendido = fila_banco.popleft()
print(cliente_atendido)

# Um comportamento interessante do deque é que podemos definir um tamanho
# máximo para ele,se esse tamanho for atingido, todos os demais items que sejam
# adicionados vão removendo os items mais antigos (posição 0), mantendo assim
# o tamanho máximo.

fila_max = deque(maxlen=5)
fila_max.append(1)
fila_max.append(2)
fila_max.append(3)
fila_max.append(4)
fila_max.append(5)
print(fila_max)

fila_max.append('a')
fila_max.append('b')
fila_max.append('c')
print(fila_max)

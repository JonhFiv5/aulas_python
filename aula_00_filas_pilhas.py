# Pilha é uma estrutura onde o último item a ser adicionado é o primeiro a ser
# removido. Imagine uma pilha de pratos, onde o último a ser colocado fica na
# parte de cima e portanto é o primeiro a ser removido.
# Em python podemos usar facilmente uma lista como se fosse uma pilha.
# Para isso basta usar as funções pop e append

lista_pilha = [1, 2, 3, 4]
# Aqui o número 5 é adicionado ao fim da lista
lista_pilha.append(5)
print(lista_pilha)
# Aqui o último elemento da lista é removido, no caso o 5, último a ser inserido
lista_pilha.pop()
print(lista_pilha)

# Um fila é uma estrutura onde o primeiro item a ser adicionado é o primeiro a
# ser removido. Imagine uma fila real, a primeira pessoa nela é a primeira a
# ser atendida.
# Apesar de podermos adicionar e remover rapidamente elementos no fim de uma
# lista, fazer isso no seu início usando isert e pop não é eficiente, isso vai
# consumir muito mais memória porque estaremos modificando as posições (índices)
# de todos os elementos da lista.
# Sendo assim, há uma forma mais eficaz de implementar filas em python, a partir
# da classe collections.deque, que permite appends e pops eficientes tanto no
# fim quanto no início da lista
from collections import deque

lista_fila = deque(['a', 'b', 'c', 'd', 'e'])
lista_fila.popleft()  # Remove o primeiro elemento a entrar na fila 'a'
lista_fila.popleft()  # Remove o segundo elemento a entrar na fila 'b'
print(lista_fila)

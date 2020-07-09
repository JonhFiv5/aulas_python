# É uma boa prática organizar nosso programa em módulos
# Deixar funções que mexem com banco de dados em um módulo, funções de cálculos
# em outro, etc.

from aulas import modulo_aula_53

lista_para_dobrar = [2, 3, 'S']
lista_dobrada = modulo_aula_53.dobra_lista(lista_para_dobrar)
print(lista_dobrada)

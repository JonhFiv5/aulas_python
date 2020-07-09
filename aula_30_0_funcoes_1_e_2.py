# Funções em Python são criadas com a palavra def
# Função simples sem parâmetros


def saudar():
    print('Fala aê')


saudar()

# Função com parâmetros


def somar(numero_1, numero_2):
    print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')


somar(10, 4)

# Se não passarmos o número esperado de argumentos ocorrerá um erro
# Podemos evitar isso definindo valores padrão, que são utilizados caso
# algum valor seja passado na chamada da função

# Parâmetros padrão


def multiplicar(numero_1=1, numero_2=1):
    print(f'{numero_1} * {numero_2} = {numero_1 * numero_2}')


multiplicar()
multiplicar(50)
multiplicar(5, 3)

# Os valores que passarmos sempre serão atribuídos na ordem em que os 
# parâmetros aparecem, se por acaso quisermos passar esses valores sem nos
# preocuparmos com ordem podemos usar argumentos nomeados


def ordenar(v_1, v_2, v_3):
    print(f'1°: {v_1}')
    print(f'2°: {v_2}')
    print(f'3°: {v_3}')


ordenar(v_3='Banana', v_1='Sorvete', v_2='Bacalhau')

# Geralmente não utilizamos print dentro uma função, ao invés disso devolvemos
# o valor com return
# Funções que não tem retorno vão devolver o valor None (o equivalente a null)


def quadrado(valor):
    return valor ** 2


resultado = quadrado(8)
print(resultado)

# Se não usarmos os parênteses podemos fazer com que uma função1 em si seja
# retornada por outra função2. E se após a chamada dessa função2 usarmos
# parênteses iremos executar a função1. Ou seja, uma executada logo após a outra


def funcao1(valor):
    print(valor)


def funcao2():
    print('A função 2 foi executada')
    return funcao1


funcao2()('Valor da função 1')
# Ao não utilizar o segundo par de parênteses, podemos atribuir a funcao1 em si
# a uma variável. Transformando essa variável em função e podendo executar ela
guarda_1 = funcao2()
guarda_1('queijo')
print(type(guarda_1))
# A variável que recebeu a função vai se tornar igual a função recebida, tanto
# que ambas vão ficar apontando para o mesmo endereço da memória
# Podemos ver o endereço através da função id()
print(f'Endereço funcao1: {id(funcao1)}\nEndereço guarda_1: {id(guarda_1)}')

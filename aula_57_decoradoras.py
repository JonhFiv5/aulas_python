# Funções decoradoras
# Uma função decoradora é uma função que adiciona funcionalidades para outra
# função, mas sem modificá-la. É uma função que envolve outra.
# Isso também é chamado de metaprogramação, porque parte do programa tenta
# modificar outra parte em tempo de compilação.

# Exemplo básico de uma função decoradora sem argumentos


def master(func):  # (Função decoradora)
    # Função de ordem superior, ela recebe a função que queremos decorar.
    print('Função mestre executada')

    def slave():  # (Função envolvedora (wrap function))
        # Função aninhada dentro da função decoradora. Nela nós colocamos
        # as funcionalidades extras para a função recebida como
        # argumento e executamos a própria função recebida.
        print('Sou uma funcionalidade extra da função', func.__name__)
        func()
        print('Também sou uma funcionalidade extra')

    return slave


def saudar():
    print('Olá mundo')


# Nessa linha nós decoramos a função saudar na função master, retornamos a
# função decorada (com as funcionalidades extras acrescentadas) e gravamos
# ela em uma variável, assim podemos usar ela quantas vezes quizermos
func_decorada = master(saudar)

print('Função saudar() original: ')
saudar()
print('\nFunção saudar() decorada: ')
func_decorada()


# Nós também podemos usar diretamente a função decorada sem ter que atribuí-la
# em uma variável antes. Para isso usamos a Pie Syntax, escrevendo o decorador
# @funcao_decoradora antes da função que queremos decorar


@master
def despedir():
    print('Adeus')


despedir()

# Para usar uma função decoradora com argumentos bastaria passar para slave e
# para function (na função mastes) *args, **kwargs

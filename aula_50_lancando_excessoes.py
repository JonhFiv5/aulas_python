# Lançando nossas próprias excessões com raise


def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as erro:
        print(erro)


# Como a excessão foi tratada dentro da função, ao fazer o try abaixo não
# acontece nada, não chega no except
try:
    dividir(1, 0)
except:
    print('Erro')


def dividir_raise(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as erro:
        print(erro)
        raise ZeroDivisionError('Houve um erro na função dividir_raise')


# Como nós usamos o raise no tratamento dentro da função, será levantada uma
# excessão que poderá ser tratada no bloco abaixo
try:
    dividir_raise(1, 0)
except ZeroDivisionError as erro:
    print('Log:', erro)

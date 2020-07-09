# Exceções personalizadas
# Por convenção as classes de exceção terminam com Error


class DeuRuimError(Exception):
    pass


def dividir(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        raise DeuRuimError('Deu ruim aqui em dividir')
    return resultado


try:
    print(dividir(15, 0))
except DeuRuimError as error:
    print(error)

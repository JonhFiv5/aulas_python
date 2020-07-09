# Usando o try except como condicionais


def converter_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        # Nós podemos usar try excepts aninhados e sequenciais, como if else
        try:
            valor = float(valor)
            return valor
        except ValueError:
            return None


num = converter_numero(input('Digite um número: '))
if num is None:
    print('Você digitou um valor inválido')
else:
    print(num * 5)

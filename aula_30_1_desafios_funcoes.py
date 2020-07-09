# 1. Recebe nome e saudação e imprime


def saudar(saudacao, nome):
    print(saudacao, nome)


saudar('Fala aí', 'mano')

# 2. Recebe três números e exibe a soma


def somar(num1, num2, num3):
    print(f'{num1} + {num2} + {num3} = {num1 + num2 + num3}')


somar(3, 4, 5)

# 3. Recebe um número e um percentual (em %), retorna o número mais o percentual


def aumentar_valor(preco, aumento):
    return preco + (preco * (aumento / 100))


valor_taxado = aumentar_valor(200, 15)
print(f'{valor_taxado:.2f}')

# Fizz Buzz - Recebe um número, caso seja divisível por 3 retorna Fizz, caso
# seja por 5 retorna Buzz, caso seja por ambos retorna FizzBuzz. Caso não seja
# por nenhum retorna o valor recebido


def fizz_buzz(numero):
    if numero % 3 == 0 == numero % 5:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    else:
        return numero


print(fizz_buzz(9))
print(fizz_buzz(20))
print(fizz_buzz(15))
print(fizz_buzz(22))

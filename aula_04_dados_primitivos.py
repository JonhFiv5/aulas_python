# Tipos de dados
# str - string
# int - inteiro
# float - real/ponto flutuante
# bool - booleano/lógico

# Podemos pegar o tipo de um dado com a função type()
print('Texto', ' -> ', type('Texto'))
print(42, ' -> ', type(42))
print(5.5, ' -> ', type(5.5))
print(0 > 2, ' -> ', type(0 > 2))

# Podemos verificar o valor lógico dos dados com a função bool()
print('Alguns elementos com valor False: ')
print('0:', bool(0))
print('String vazia:', bool(''))
print('Array vazio:', bool([]))
print('Tupla vazia:', bool(()))
print('Dicionário vazio:', bool({}))

# A função acima é um exemplo de casting, quando mudamos o tipo de um dado
# Outras formas de casting:
print("23", ' -> ', type(str(23)))
print("'42'", ' -> ', type(int('42')))
print("12", ' -> ', type(float(12)), '=', float(12))
# Converter float em int causa perda de informação
print("10.5", ' -> ', type(int(10.5)), '=', int(10.5))

# Só podemos converter valores compatíveis, não dá pra transformar
# um caractere em um número

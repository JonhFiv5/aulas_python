# Usando list comprehension, separar a string abaixo em grupos de 0 a 9
# lista = ['0123456789', '0123456789'. etc...]
# Depois disso, retornar uma única string com o seguinte formato:
# retorno = '0123456789.0123456789.0123456789... etc'
string = '012345678901234567890123456789012345678901234567890123456789'

'''
lista = []
palavra = ''
for elemento in string:
    palavra += elemento
    if elemento == '9':
        lista.append(palavra)
        palavra = ''

retorno = '.'.join(lista)
'''

lista = [string[i * 10:(i + 1) * 10] for i in range(0, int(len(string) / 10))]
retorno = '.'.join(lista)

print(retorno)
# Saída: 0123456789.0123456789.0123456789.0123456789.0123456789.0123456789

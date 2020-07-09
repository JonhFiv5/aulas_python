# Validador de CNPJ compacto
# Exemplos de CNPJ:
# 04.252.011/0001-10
# 40.688.134/0001-61
# 71.506.168/0001-11
# 12.544.992/0001-05
import re
from copy import deepcopy


def calcula_digito(soma):
    digito = 11 - (soma % 11)
    return digito if digito <= 9 else 0


cnpj_original = "12.544.992/0001-05"
numeros = re.sub(r'[^0-9]', '', cnpj_original)
numeros_lista = [int(numero) for numero in numeros[0:-2]]

inicio = 5
for digi in range(0, 2):
    total = 0
    copia_lista = deepcopy(numeros_lista)
    for i in range(inicio, 1, -1):
        total += i * copia_lista.pop(0)
        if i == 2:
            for j in range(9, 1, -1):
                total += j * copia_lista.pop(0)
    numeros_lista.append(calcula_digito(total))
    inicio += 1

cnpj_final = re.sub(r'[^0-9]', '', str(numeros_lista))
valido = numeros == cnpj_final
print('CNPJ válido.' if valido else 'CNPJ inválido.')

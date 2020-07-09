# Módulo importado no arquivo da aula 60
import re  # Expressão regular
from copy import deepcopy


def extrair_numeros_cnpj(cnpj):
    """
    Extrai os demais caracteres do cnpj, retornando apenas o números
    :param cnpj: cnpj original
    :type cnpj: str
    :return: números do cnpj
    :rtype: str
    """
    cnpj_formatado = re.sub(r'[^0-9]', '', cnpj)
    return cnpj_formatado


def encontrar_soma(cnpj, digito=1):
    """
    Calcula a soma das multiplicações necessárias para se encontrar um dos dois
    dígitos de um cnpj
    :param cnpj: resultante da função listar_cnpj()
    :param digito: 1 para o primeiro dígito, 2 para o segundo dígito
    :type cnpj: list
    :type digito: int
    :return: total
    :rtype: int
    """
    copia_cnpj = deepcopy(cnpj)
    inicio = 0
    if digito == 1:
        inicio = 5
    elif digito == 2:
        inicio = 6
    total = 0
    for i in range(inicio, 1, -1):
        total += i * copia_cnpj.pop(0)
        if i == 2:
            for j in range(9, 1, -1):
                total += j * copia_cnpj.pop(0)
    return total


def listar_cnpj(cnpj):
    """
    Espalha os dígitos do cnpj em uma lista

    :param cnpj: resultante da função extrair_numeros_cnpj()
    :type cnpj: str
    :return: numeros_cnpj
    :rtype: list
    """
    numeros_cnpj = [int(numero) for numero in cnpj]
    return numeros_cnpj


def calcular_digito(soma_calculo):
    """
    Fórmula para encontrar o valor do dígito de acordo com o total do cálculo

    :param soma_calculo: resultado da soma encontrado
    pela função encontrar_soma()
    :type soma_calculo: int
    :return: dígito encontrado através da fórmula
    :rtype: int
    """
    digito = 11 - (soma_calculo % 11)
    return digito if digito <= 9 else 0


def encontrar_digitos(cnpj):
    """
    :param cnpj: lista resultante de listar_cnpj()
    :type cnpj: list
    :return: os dois dígitos do cnpj
    :rtype: list
    """
    digito_1 = calcular_digito(encontrar_soma(cnpj, 1))
    cnpj.append(digito_1)
    digito_2 = calcular_digito(encontrar_soma(cnpj, 2))
    return [digito_1, digito_2]


def incluir_digitos_cnpj(cnpj, digitos):
    """

    :param cnpj: apenas os números do cnpj
    :type cnpj: str
    :param digitos: array, os dois dígitos finais do cnpj
    :return:
    """
    cnpj += str(digitos[0])
    cnpj += str(digitos[1])
    return cnpj


def reformatar_cnpj(cnpj_completo):
    """
    Reinsere os caracteres especiais no cnpj
    :param cnpj_completo: o cnpj completo com os dois dígitos
    :type cnpj_completo: str
    :return: o cnpj com a formatação completa
    40.688.134/0001-61
    01.234.567/89
    """
    c = cnpj_completo
    return f'{c[0:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}'


def montar_digitos_cnpj(cnpj):
    """
    Executa todas as funções necessárias para obter o cnpj completo
    :param cnpj: cnpj original sem formatação e sem os dígitos
    :type cnpj: str
    :return: cnpj completo após todos os cálculos
    :rtype str
    """
    cnpj_formatado = extrair_numeros_cnpj(cnpj)
    cnpj_listado = listar_cnpj(cnpj_formatado)
    digitos = encontrar_digitos(cnpj_listado)
    cnpj_final = incluir_digitos_cnpj(cnpj_formatado[0:-2], digitos)
    cnpj_formatado = reformatar_cnpj(cnpj_final)
    return cnpj_formatado


def verificar_cnpj(cnpj_original, cnpj_processado):
    if cnpj_original == cnpj_processado:
        return "CNPJ válido."
    else:
        return "O CNPJ informado é inválido."

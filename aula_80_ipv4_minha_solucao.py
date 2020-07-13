# Cálculo de IPV4, código feito sem ver a solução do professor
def converter_em_binario(num_decimal: int) -> str:
    _valores = [128, 64, 32, 16, 8, 4, 2, 1]

    num_binario = ''
    soma = 0
    for valor in _valores:
        temp_soma = soma + valor
        if valor <= num_decimal and temp_soma <= num_decimal:
            num_binario += '1'
            soma += valor
        else:
            num_binario += '0'

    return num_binario


def converter_em_decimal(num_binario: str) -> int:
    _valores = [128, 64, 32, 16, 8, 4, 2, 1]

    num_decimal = 0
    for i, bit in enumerate(num_binario):
        if bit == '1':
            num_decimal += _valores[i]

    return num_decimal


def mascara_binario(mascara_num: int) -> tuple:
    bits_mascara = ''.join(['1' for i in range(mascara_num)])
    num_bits_host = 32 - len(bits_mascara)
    for bit in range(num_bits_host):
        bits_mascara += '0'
    return bits_mascara, num_bits_host


def dividir_grupos(sequencia_bin: str) -> tuple:
    g_1 = sequencia_bin[0:8]
    g_2 = sequencia_bin[8:16]
    g_3 = sequencia_bin[16:24]
    g_4 = sequencia_bin[24:]
    return g_1, g_2, g_3, g_4


def calcular_hosts(num_bits_host):
    return (2 ** num_bits_host) - 2


def formatar_ip(sequencia_bits, mascara):
    ip_f = [converter_em_decimal(n) for n in dividir_grupos(sequencia_bits)]
    return f'{ip_f[0]}.{ip_f[1]}.{ip_f[2]}.{ip_f[3]}/{mascara}'


def calcular_primeiro_ip(sequencia_bits, mascara):
    ip_f = [converter_em_decimal(n) for n in dividir_grupos(sequencia_bits)]
    return f'{ip_f[0]}.{ip_f[1]}.{ip_f[2]}.{ip_f[3] + 1}/{mascara}'


def calcular_ultimo_ip(sequencia_bits, mascara):
    ip_f = [converter_em_decimal(n) for n in dividir_grupos(sequencia_bits)]
    return f'{ip_f[0]}.{ip_f[1]}.{ip_f[2]}.{ip_f[3] - 1}/{mascara}'


def formatar_mascara(sequencia_bits):
    ip_f = [converter_em_decimal(n) for n in dividir_grupos(sequencia_bits)]
    return f'{ip_f[0]}.{ip_f[1]}.{ip_f[2]}.{ip_f[3]}'


def calcula_rede_broadcast(bits: str, bits_hosts: int, digito: str):
    lista_bits = list(bits)[::-1]
    for i in range(bits_hosts):
        lista_bits[i] = digito
    ip_calculado = ''.join(lista_bits[::-1])
    return ip_calculado


ip = '10.20.12.45/26'
grupo_1 = converter_em_binario(10)
grupo_2 = converter_em_binario(20)
grupo_3 = converter_em_binario(12)
grupo_4 = converter_em_binario(45)

ip_bin = grupo_1 + grupo_2 + grupo_3 + grupo_4

mascara_bin, numero_bits_host = mascara_binario(26)

rede_bin = calcula_rede_broadcast(ip_bin, 6, '0')
broadcast_bin = calcula_rede_broadcast(ip_bin, 6, '1')

print('IP '.ljust(20, '-'), ip)
print('Rede '.ljust(20, '-'), formatar_ip(rede_bin, 26))
print('Broadcast '.ljust(20, '-'), formatar_ip(broadcast_bin, 26))
print('Máscara '.ljust(20, '-'), formatar_mascara(mascara_bin))
print('Primeiro IP '.ljust(20, '-'), calcular_primeiro_ip(rede_bin, 26))
print('Último IP '.ljust(20, '-'), calcular_ultimo_ip(broadcast_bin, 26))
print('Hosts totais '.ljust(20, '-'), calcular_hosts(numero_bits_host) + 2)
print('Hosts disponíveis '.ljust(20, '-'), calcular_hosts(numero_bits_host))

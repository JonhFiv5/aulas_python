# Vamos percorrer arquivos e pastas usando o módulo os
# Esse código vai buscar arquivos em determinado diretório

import os


def formata_tamanho(tamanho_bytes):
    """Serve para mostrar o tamanho formatado dos arquivos"""
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho_bytes < kilo:
        texto = 'B'
    elif tamanho_bytes < mega:
        tamanho_bytes /= kilo
        texto = 'K'
    elif tamanho_bytes < giga:
        tamanho_bytes /= mega
        texto = 'M'
    elif tamanho_bytes < tera:
        tamanho_bytes /= giga
        texto = 'G'
    elif tamanho_bytes < peta:
        tamanho_bytes /= tera
        texto = 'T'
    else:
        tamanho_bytes /= peta
        texto = 'P'

    tamanho_bytes = round(tamanho_bytes, 2)
    return f'{tamanho_bytes} {texto}'


caminho = '/home/joao/Programacao/CursoPython/exercicios_python'
pesquisa = 'py'  # Arquivos que contém 'py' no nome ou extensão

arquivos_encontrados = 0

# Com a função walk nós percorremos todos os arquivos no diretorio especificado
# E todos os arquivos dentro de cada subdiretório dentro daquele.
for raiz, diretorios, arquivos in os.walk(caminho):
    # raiz - o nome do diretório atual
    # diretorios - os subdiretórios dentro do diretório atual
    # arquivos - os arquivos no diretório atual
    for arquivo in sorted(arquivos):
        if pesquisa in arquivo:
            try:
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)

                print(f'\nArquivo encontrado: {arquivo}')
                print(f'Caminho: {caminho_completo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {extensao_arquivo}')
                print(f'Tamanho: {formata_tamanho(tamanho_arquivo)}')

                arquivos_encontrados += 1
            except Exception as error:
                print('A pesquisa não pôde ser concluída.')
                print('Erro: ', error)

print(f'\n{arquivos_encontrados} arquivo(s) encontrado(s).')

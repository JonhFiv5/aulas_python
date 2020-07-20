# Mover, apagar e copiar arquivos

import os
import shutil
import time

# Caminho onde se encontra o arquivo
caminho_original = '/home/joao/Desktop'

# Caminho para onde vamos mover ele
caminho_novo = '/home/joao/Desktop/teste'

# O caminho_novo ainda nã existe, então criamos a pasta com o seguinte comando
try:
    os.mkdir(caminho_novo)
except FileExistsError as error:
    print(f'O diretório {caminho_novo} já existe.')
except Exception as error:
    print(error)

for raiz, diretorios, arquivos in os.walk(caminho_original):
    for arquivo in arquivos:
        if 'txt' in arquivo:
            time.sleep(0.5)
            # Pegamos o caminho completo do arquivo
            old_path = os.path.join(raiz, arquivo)

            # Pegamos o caminho completo para onde vai o arquivo
            new_path = os.path.join(caminho_novo, arquivo)

            # Esse comando também consegue renomear arquivos, é só mover
            # para a mesma pasta, mas com um nome diferente no caminho
            # shutil.move(old_path, new_path)

            # Comando para copiar os arquivos
            # shutil.copy(old_path, new_path)

            # Comando para apagar os arquivos
            # os.remove(new_path)

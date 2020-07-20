from zipfile import ZipFile
import os

caminho = '/home/joao/Programacao/CursoPython/aulas_python'
# Se estiver no windows para usar \ escreve r'C:\Etc\Etc..'

# Zipar um arquivo
with ZipFile('aula_92.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        if 'aula_92.txt' == arquivo:
            # Primeiro passamos o caminho (o arquivo em si) e depois como
            # queremos que seja salvo, senão ele também vai salvar toda a
            # estrutura de pastas e não só o arquivo.
            zip.write(caminho_completo, arquivo)

# Listar um zip
with ZipFile('aula_92.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Descompactar
with ZipFile('aula_92.zip', 'r') as zip:
    zip.extractall('aula_92_descompactado')

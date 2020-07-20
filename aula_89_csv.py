# CSV - Comma Separated Values é um formato de dados muito usado em tabelas
# (excel, google sheets), bases de dados, clientes de e-mail, etc...

import csv

# Lendo um arquivo CSV
with open('aula_89_produtos.csv', 'r') as file:
    # dados = csv.reader(file)  # Devolve em forma de lista
    # dados = csv.DictReader(file)  # Devolve em forma de dicionário
    dados = [x for x in csv.DictReader(file)]

    # Como dados é um gerador, ele deixa de ser acessível fora do escopo do
    # with, depois que o arquivo é fechado. Então podemos transformá-lo em
    # uma lista se quisermos ter esses dados depois

    for dado in dados:
        print(dado)

print(dados)

# Agora para escrever um arquivo CSV é preciso criar algumas configurações
# com o método writer, que vai criar uma instância 'escrever'
with open('aula_89_produtos2.csv', 'w') as file:
    escrever = csv.writer(
        file,  # Passamos o arquivo
        delimiter=',',  # O delimitador das células
        quotechar='"',  # Define o caractere para aspas
        quoting=csv.QUOTE_ALL  # (opcional) vai envolver os dados com aspas
    )

    # Para passar o cabeçalho da tabela precisamos pegar as chaves
    chaves = list(dados[0].keys())
    escrever.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
        ]
    )

    # Agora percorremos nossa lista com dicionários, escrevendo os valores no
    # arquivo
    for dado in dados:
        escrever.writerow(
            [
                dado['Nome'],
                dado['Preço'],
                dado['Quantidade'],
            ]
        )

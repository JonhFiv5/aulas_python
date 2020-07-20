# Basicamente é pegar dados de um site
# Útil quando o site não fornece uma API para isso

# Nesse arquivo:
# Do link: https://stackoverflow.com/questions/tagged/python
# Pegar o título, a data e os votos de cada pergunta
# !NOTA! Em cada site a forma de acessar os dados é diferente

# Instalamos via pip o requests e o beautifulsoup4

import requests  # Vai fazer as requisições
from bs4 import BeautifulSoup  # Vai permitir manipular o HTML

url = 'https://pt.stackoverflow.com/questions/tagged/python'

# Pegamos o HTML da página
response = requests.get(url)

# Criamos um objeto BeautifulSoup, passando o HTML (response.text) e o tipo de
# dado que estamos analisando (html.parser)
html = BeautifulSoup(response.text, 'html.parser')

# Percorremos as tags que tem essa classe css
for pergunta in html.select('.question-summary', ):

    # Pegamos o título, que tem a classe .question-hyperlink
    titulo = pergunta.select_one('.question-hyperlink')

    # Pegamos a data, na classe .relativetime
    data = pergunta.select_one('.relativetime')

    # Pegamos o valor em si da data, que está dentro do atributo title
    # attrs é um dicionário com os atributos daquela tag
    data_valor = data.attrs['title']

    votos = pergunta.select_one('.vote-count-post')

    # Via text pegamos apenas o valor da tag, que é o texto dela
    print('Pergunta: ', titulo.text)
    print('Votos: ', votos.text)
    # print('Data: ', data_valor, end='\n\n')
    print('Data: ', data.text, end='\n\n')

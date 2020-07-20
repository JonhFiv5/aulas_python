# Trabalhando com data e hora com o módulo datetime

from datetime import datetime, timedelta
# Timedelta se refere a intervalo de tempo

# Podemos criar uma data passando, por exemplo, esses argumentos
data = datetime(year=2020, month=7, day=14, hour=7, minute=32, second=15)

# Imprimindo diretamente a data é mostrado em formato americano
# Geralmente é salvo assim no BD
print('Formato padrão: ', data)

# Para customizar a exibição usamos o método strftime(), e dentro dele
# passamos uma máscara de letras antecedidas por porcentagem (diretivas).
# %d indica dia, %m = mês, %Y = ano completo, %H = hora, %M = minuto.
# No fim da documentação de datetime encontramos mais diretivas e o que cada
# uma faz na máscara.
# Esse método de customização também é usado no relógio do Linux Mint.
print('Formato customizado: ', data.strftime('%d/%m/%Y %H:%M:%S'))

# Podemos converter uma string para uma data com a função strptime
# Ela recebe a string da data e o formato em que ela está

texto_data = datetime.strptime('22/06/1999', '%d/%m/%Y')
print('String convertida: ', texto_data)

# Também podemos trabalhar com timestamp, uma função que retorna o valor
# em segundos entre 01/01/1970 e a data em questão
# É possível pegar o timestamp de uma data e transformar uma data em
# timestamp.
# Algumas vezes é salvo o timestamp no BD ao invés do formato data

# Pegando o timestamp de uma data
time_s = datetime.timestamp(texto_data)
print('Timestamp de 22/06/1999: ', time_s)

# Pegando uma data a partir de um timestamp com a função fromtimestamp()
data_s = datetime.fromtimestamp(time_s)
print('Data recuperada do timestamp', data_s)

# Cálculos com datas usando timedelta -----------------------
data_delta = datetime.strptime('30/05/2020 15:00:00', '%d/%m/%Y %H:%M:%S')
print(data_delta.strftime('%d/%m/%Y %H:%M:%S'))

# Acrescentando três dias
data_delta = data_delta + timedelta(days=3)
print(data_delta.strftime('%d/%m/%Y %H:%M:%S'))

# Acrescentando trinta minutos
data_delta = data_delta + timedelta(minutes=30)
print(data_delta.strftime('%d/%m/%Y %H:%M:%S'))

# Cálculo entre datas --------------------------------------
data_1 = datetime(day=2, month=3, year=2020, hour=10)
data_2 = datetime(day=20, month=3, year=2020, hour=15, minute=45)

# Diferença de dias (é a única operação possível por padrão)
dif = data_2 - data_1
print(dif)

# Também podemos aplicar operadores relacionais
print('A maior data é a', 'primeira' if data_1 > data_2 else 'segunda')

# Pegando o último dia de um mês

# mdays é uma lista com o número de dias de cada mês
# ela tem 13 valores, o primeiro é 0. Então se pegarmos o índice 1, vai nos
# retornar o número de dias de janeiro
from calendar import mdays, monthrange
from datetime import datetime

data_atual = datetime.now()
mes_atual = data_atual.month
ultimo_dia = mdays[mes_atual]
print(f'O último dia do mês {mes_atual} é {ultimo_dia}')

# Entretanto, como é uma lista o mdays não funciona bem em anos bissextos
# Aí entra a função monthrange.
# Ela vai receber o ano(int) e o mês(int) e retorna uma tupla contendo o número
# do dia atual na semana (segunda = 0) e o número do último dia do mês

# Aqui podemos ver que fevereiro tem 29 dias em 2020
print(monthrange(2020, 2))
# O que não funcionario com mdays, já que é uma lista fixa
print(mdays[2])

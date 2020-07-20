# Datas em português
# Vamos tentar imprimir:
# Terça, 14 de Julho de 2020

from datetime import datetime
from locale import setlocale, LC_ALL

# Nessa linha nós indicamos o local, ou seja, o idioma da máquina.
# Então ao imprimir o nome de dias e meses sairá em português
setlocale(LC_ALL, 'pt_BR.utf-8')

data = datetime.now()
formatacao = '%A, %d de %B de %Y'
# %A = nome do dia
# %d = número do dia
# %B = nome completo do mês
# %Y = ano completo

data_ingles = datetime.strftime(data, formatacao)

print(data_ingles)
# O %x vai imprimir a data de acordo com o formato padrão do local
print(datetime.strftime(data, '%x'))

# O %c vai imprimir a data e hora de acordo com o formato padrão do local
print(datetime.strftime(data, '%c'))

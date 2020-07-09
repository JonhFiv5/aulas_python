# Iterando(percorrendo) string
from time import sleep

minha_string = 'Tangamandápio'

contador = 0
while contador < len(minha_string):
    print(minha_string[contador])
    contador += 1

# A string é imutável em python, o código abaixo não roda
# minha_string[0] = 'V'

meu_texto = 'PIPOCA_DOCE'
meu_texto_2 = ''
contador = 0
while contador < len(meu_texto):
    meu_texto_2 += meu_texto[contador]
    print(f'{meu_texto_2:>30}', end='|')
    print(f'{meu_texto_2[::-1]:<30}')
    sleep(0.3)
    contador += 1

# Criando nossa função capitalize improvisada
frase_minuscula = 'era uma vez duas coisas e três pipocas'
frase_capitalizada = ''
contador = 0
proxima_maiuscula = False
while contador < len(frase_minuscula):
    if contador == 0 or proxima_maiuscula:
        frase_capitalizada += frase_minuscula[contador].upper()
    else:
        frase_capitalizada += frase_minuscula[contador]
    if frase_minuscula[contador] == ' ':
        proxima_maiuscula = True
    else:
        proxima_maiuscula = False
    contador += 1
print(frase_capitalizada)

# Validador de CNPJ
# Exemplos de CNPJ:
# 04.252.011/0001-10
# 40.688.134/0001-61
# 71.506.168/0001-11
# 12.544.992/0001-05

# Encontrando o primeiro dígito:
# 1. Espalhamos os 12 primeiros número de um CNPJ
# 2. Embaixo, iniciamos uma contagem de 5 à 2, depois de 9 à 2
# 3. Multiplicamos os números de cima pelos de baixo
# 4. Somamos os resultados
#    0  4  2  5  2  0  1  1  0  0  0  1    ->Primeiro passo
#    5  4  3  2  9  8  7  6  5  4  3  2    ->Segundo passo
#    0  16 6  10 18 0  7  6  0  0  0  2    ->Terceiro passo
#       16 + 6 + 10 + 18 + 7 + 6 + 2 = 65  ->Quarto passo
# 5. Depois aplicamos o resultado na fórmula e encontramos o primeiro dígito:
# 11 - (65 % 11) = 1 (Se o dígito for maior que 9 se torna 0)

# Encontrando o segundo dígito:
# É da mesma forma que no exemplo acima, mas com duas diferenças:
# 1. Ao fim dos 12 números você vai adicionar também o dígito encontrado acima
# 2. Como há um número a mais, a contagem vai ir de 6 à 2 e de 9 à 2

# ORIENTAÇÃO - Escrever o código em um módulo e quebrar as funcionalidades dele
# em funções.

import aulas.aula_60_valida_cnpj as valida

cnpj = '40.688.134/0001-61'
cnpj_encontrado = valida.montar_digitos_cnpj(cnpj)
print(valida.verificar_cnpj(cnpj, cnpj_encontrado))

# Verificar se uma string pode ser convertida em número
# isnumeric isdigit isdecimal

# isdecimal - retorna True se todos os caracteres forem decimais
print('-12'.isdecimal())  # Falso, devido ao sinal de -
print('7.5'.isdecimal())  # Falso, devido ao ponto
print('122'.isdecimal())  # Verdadeiro

print(123456)  # Pode receber  só um argumento
print('João', 'Kaíque')  # Pode receber vários argumentos
print('João', 'Kaíque', sep='-')  # Argumentos nomeados (separador)
print('Era uma vez', end=' ')  # Argumento para continuar no próximo print()
print('uma gaiola verde.')
# Print() não rola, python é case sensitive

# Exercicio: Escrever o CPF '824.173.070-18' usando sep e end
print('824', '173', '070', sep='.', end='-')
print('18')

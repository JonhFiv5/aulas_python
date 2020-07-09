user = input('Insira seu nome de usuário: ')
password = input('Insira sua senha: ')


# Função len() personalizada
def numero_caracteres(texto):
    tamanho_total = 0
    for caracter in texto:
        tamanho_total += 1
    return tamanho_total


# Utilizamos a função len() para saber o tamanho de uma string
if len(password) < 8:
    print('Senha muito curta!')
else:
    print(f'Seja bem-vindo de volta {user}!')

print(f'len: {len(password)}')
print(f'numero_caracteres: {numero_caracteres(password)}')

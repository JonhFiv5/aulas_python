# Realiza as ações no bloco enquanto a condição for verdadeira

while True:  # Loop infinito
    nome = input('Qual o seu nome? ')
    if len(nome) > 15:
        break  # Código que interrompe o loop
print('Acabou 1')

# A palavra reservada 'continue' serve para ignorar o resto do código e pular
# para a próxima iteração
num = 0
while num <= 10:
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1
print('Acabou 2')

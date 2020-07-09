# Split = Dividir uma string (str)
# Join = Juntar uma lista (str)
# Enumerate = Enumerar elementos da lista (list/iteráveis)

# split() divide a string em uma lista de acordo com o separador informado
texto = 'O rato roeu a roupa do rei de roma'
print(texto.split(' '))
print(list(texto.replace(' ', '')))  # Assim podemos dividir letra por letra

# join() junta uma lista em uma string, é o oposto de split()
# Antes do join digitamos o caractere que vai fazer a junção
vogais = ['a', 'e', 'i', 'o', 'u']
print('-'.join(vogais))

# enumerate - uma forma rápida de conseguir um contador
# O primeiro valor é o índice e o segundo o elemento
lista = ['carro', 'sapato', 'cavalo']
for indice, valor in enumerate(lista):
    print(f'{indice} => {valor}')

# Lista dentro de lista
lista_com_listas = [
    ['Queijo', 'Presunto', 'Pão'],
    ['Banana', 'Abacate', 'Maça'],
    ['Azul', 'Vermelho', 'Preto']
]

for lista in lista_com_listas:
    for indice, elemento in enumerate(lista):
        print(f'[{indice}]{elemento}')

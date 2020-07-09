# Expressão condicional com o operador or (ou)
# nome = input('Digite seu nome: ')
# print(nome or 'Você não digitou nada...')

# O or pode detectar rapidamente valores não falsos
a = 0
b = None
c = False
d = []
e = {}
f = 15
g = 'joão'
# A variável vai assumir o primeiro valor verdadeiro (no caso, o que não está
# vazio)
valor = a or b or c or d or e or f or g or None
print(valor)
# Não importa se houver outros depois, vai pegar logo o primeiro
valor = a or b or 'Vazio' or g
print(valor)

# Pela forma tradicional 
# Ficaria assim:
valor = a or b or c or d or e or f or g or None

if a:
    valor = a
elif b:
    valor = b
elif c:
    valor = c
elif d:
    valor = d
elif e:
    valor = e
elif f:
    valor = f
elif g:
    valor = g
else:
    valor = None

print(valor)

# Concluimos então que o operador or pode ser uma alternativa interessante ao
# if/elif

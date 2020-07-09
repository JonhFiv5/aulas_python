# Podemos adicionar um else a um laço for, esse bloco do else só é executado se
# o laço chegar até o fim com sucesso, sem que haja um break

letras = ['a', 'b', 'c', 4, 'd', 'e']
for letra in letras:
    if str(letra).isnumeric():
        break
    print(letra)
else:
    print('Se eu não aparecer é porque o break foi executado')

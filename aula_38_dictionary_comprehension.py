# Compreensão de dicionários

precos = {
    'preco1': 25,
    'preco2': 15,
    'preco3': 17,
    'preco4': 31,
}

# Aplicamos um desconto de 5% para todos os preços
# Também fatiamos as chaves pra mostrar que podemos alterar os dois valores
precos_desconto = {
    'valor_' + str(i + 1): precos[chave] * 0.95
    for i, chave in enumerate(precos)}
print(precos_desconto)

# Lembrando que como valores colocados entre chaves, mas sem pares também são
# considerados sets, é assim que fazemos set comprehension:
set_qualquer_coisa = {'_' + valor.upper() + '_' for valor in 'Pipoca'}
print(sorted(list(set_qualquer_coisa)))

# Desafio: Pegar o total dos produtos armazenados do carrinho de compras
# usando list comprehension

carrinho_compras = [
    ('Produto1', 28),
    ('Produto2', 19),
    ('Produto3', 15),
    ('Produto4', 32),
]

total = sum([tupla[1] for tupla in carrinho_compras])
print(total)

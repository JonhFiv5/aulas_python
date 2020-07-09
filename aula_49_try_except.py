# Tratando excessões em Python com try except

# Nós podemos tratar erros de uma forma mais geral, sem especificar um
# determinado erro e pegando qualquer um que ocorre, mas isso não o ideal

try:
    print(variavel_nao_declarada)
except Exception as erro:
    print(erro)

try:
    print(1 / 0)
except ZeroDivisionError as erro:
    print('Erro, não existe divisão por zero.')

# Podemos tratar dois erros numa única excessão:
try:
    # a = 1 / 0
    # Só o primeiro erro ocorrerá, o resto do código antes do except será
    # ignorado
    print(b)
except (ZeroDivisionError, NameError) as erro:
    print(erro)

# Podemos adicionar um else no fim, ele só será executado se não acontecer
# nenhuma excessão no try
try:
    a = 'b' + 2
except TypeError as erro:
    print(erro)
else:
    print('Bacon')

# Também podemos ter um finally, que será executado de qualquer forma
try:
    a = [1, 2, 3, 4]
    # a = []
    print(a[2])
except IndexError as erro:
    print(erro)
else:
    print('Abacate')
finally:
    print('Pipoca')

# Também é possível ter excepts sucessivos, e escolher entre else e finally, não
# precisa ter os dois

try:
    dici = {}
    print(dici['Chave'])
except NameError as erro:
    print(erro)
except TypeError as erro:
    print(erro)
except KeyError as erro:
    print('A chave não exite.')
finally:
    print('Tratamento concluído')

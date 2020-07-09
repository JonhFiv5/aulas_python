# Criar dois contadores dentro do mesmo laço
# Uma vai de 0 a 8 e o outro de 10 a 2


for progressivo, regressivo in enumerate(range(10, 1, -1)):
    print(progressivo, regressivo)

# regressivo vai guardar o valor devolvido pela função range
# progressivo vai guardar o valor de enumerate, o número de iterações

# count itertools
# A função count gera um contador que é um iterador

from itertools import count

# Aqui é gerado um contador que não tem fim, sempre vai incrementando +1
contador = count()
print(next(contador))
print(next(contador))

# É preciso ter cuidado ao trabalhar com um contador infinito
for i in contador:
    if i == 10000:
        print('É mais de 8000!!!')
        break

# A função count pode receber dois valores, o start=x que recebe o valor inicial
# e o step=x que determina o incremento ou decremento. Embora a função espere um
# número inteiro, também vai funcionar com um decimal

cont_dec = count(start=5, step=0.25)
for i in cont_dec:
    print(i)
    if i >= 6:
        break

cont_range = range(2000)
for i in cont_range:
    if i == 1500:
        print('Break')
        break

# A diferença entre range e count é que o count não possui um fim específico e
# funciona com float no step. Enquanto o range obrigatoriamente precisa receber
# um valor para o fim e só aceita int no step.

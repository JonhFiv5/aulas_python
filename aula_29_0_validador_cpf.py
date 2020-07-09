# Passos para calcular o penúltimo dígito do CPf:
# 1: Pegar os nove primeiros números
# 2: Multiplicar de 10 a 2, ex: primeiro número * 10, segundo * 9, etc
# 3: Pegar a soma dos resultados
# 4: Pegar resultado da fórmula: 11 - (soma % 11) (11 é o tamanho de um CPF)
# 5: Se o resultado for maior que 9, pegamos o 0. Se for igual ou menor vai ser
# o próprio resultado mesmo.

# Calcular o último dígito do CPf:
# Como antes, pegamos os nove primeiros dígitos do CPF, mas dessa vez também
# vamos pegar o décimo, que é o resultado do cálculo acima.
# A multiplicação regressiva vai ser de 11 a 2, já que temos um número a mais
# E o resto segue da mesma forma que já foi explicada

cpf = str(input('Digite o seu CPF: ')).strip().replace('.', '').replace('-', '')
novo_cpf = cpf[0:9]
soma = 0

# Calculando o décimo dígito
for progressivo, regressivo in enumerate(range(10, 1, -1)):
    soma += int(novo_cpf[progressivo]) * regressivo

novo_cpf += str(0 if 11 - (soma % 11) > 9 else 11 - (soma % 11))
soma = 0

# Calculando o décimo primeiro dígito
for progressivo, regressivo in enumerate(range(11, 1, -1)):
    soma += int(novo_cpf[progressivo]) * regressivo

novo_cpf += str(0 if 11 - (soma % 11) > 9 else 11 - (soma % 11))

print('CPF válido' if cpf == novo_cpf else 'CPF inválido.')

# A função filter irá percorrer o iterável retornando apenas os elementos
# que atendem às condições definidas.
# Ele vai receber uma função com retorno lógico, se for True o elemento será
# considerado pelo filter, se for False será ignorado

lista_nomes = ['Ana', 'Pedro', 'Thiago', 'Alberto', 'Tamires', 'André']
nomes_inicial_a = list(filter(lambda nome: nome[0] == 'A', lista_nomes))
print(nomes_inicial_a)

clientes = [
    {'Nome': 'Ana', 'Sexo': 'F', 'Idade': 23},
    {'Nome': 'André', 'Sexo': 'M', 'Idade': 16},
    {'Nome': 'Júlia', 'Sexo': 'F', 'Idade': 17},
    {'Nome': 'Cláudio', 'Sexo': 'M', 'Idade': 28},
    {'Nome': 'Pedro', 'Sexo': 'M', 'Idade': 27},
    {'Nome': 'Bruna', 'Sexo': 'F', 'Idade': 25},
    {'Nome': 'Carla', 'Sexo': 'F', 'Idade': 12},
    {'Nome': 'Natan', 'Sexo': 'M', 'Idade': 15},
    {'Nome': 'Jorge', 'Sexo': 'M', 'Idade': 18},
    {'Nome': 'Amanda', 'Sexo': 'F', 'Idade': 18},
]


def filtrar_homens_adultos(cliente):
    if cliente['Sexo'] == 'M' and cliente['Idade'] >= 18:
        return True
    else:
        return False


cl_homens_adultos = list(filter(filtrar_homens_adultos, clientes))
for registro in cl_homens_adultos:
    print(registro)

# Pode ocorrer da função filter devolver os mesmos elementos que recebeu, no
# entanto quando se utiliza é esperado que seja retornado um número menor.

# Nós também podemos criar um arquivo json a partir de um dicionário
import json

registro = {
    'nome': 'Godofredo',
    'idade': 47,
    'sexo': 'M',
    'altura': 1.65,
    'peso': 76,
    'nacionalidade': 'Portugues'
}

# Convertendo em json (o atributo indent é pra deixar organizado)
registro_json = json.dumps(registro, indent=True)

# Criando um arquivo json
with open('aula_56_teste.json', 'w') as file:
    file.write(registro_json)

# Recuperando um json para um dicionário
with open('aula_56_teste.json', 'r') as file:
    # Recebendo o json
    dicio_arquivo = file.read()
# Convertendo em dicionário
dicio_arquivo = json.loads(dicio_arquivo)
print(type(dicio_arquivo))

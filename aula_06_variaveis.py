# Variáveis em python devem:
# *Iniciar com letras
# *Pode conter números
# *Não pode conter espaços ou caracteres especiais
# *Não podem conter acentuação
# *As palavras são separadas com underscore snake_case
# *Conter nomes curtos e bem claros
# *Todas as letras minúsculas

# A tipagem é dinâmica, não precisamos definir o tipo na declaração da variável
texto = 'João'
numero_inteiro = 5
casa_flutuante = 18.23
valor_logico = 1 == '1'

print(texto, '=>', type(texto))
print(numero_inteiro, '=>', type(numero_inteiro))
print(casa_flutuante, '=>', type(casa_flutuante))
print(valor_logico, '=>', type(valor_logico))

# Nota: Docstrings também são válidas como strings
valor_estranho = """Bacon"""
print(valor_estranho)

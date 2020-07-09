from aulas.vendas_54.calc_preco import aumentar_preco, reduzir_preco
import aulas.vendas_54.formata.preco as form_preco

valor_1 = aumentar_preco(valor=200, porcentagem=15)
valor_2 = reduzir_preco(valor=100, porcentagem=7)

print(form_preco.formatar_preco(valor=valor_1))
print(form_preco.formatar_preco(valor=valor_2))

# Nesse módulo (importado no arquivo 53_criando_modulos.py) criamos uma função
# Para testes


def dobra_lista(lista):
    dobro_lista = [valor * 2 for valor in lista]
    return dobro_lista


# Código testando a função
# Sempre que importássemos o módulo por inteiro esse código dentro dele que
# serve apenas para testes seria executado. Para evitar isso nós podemos
# verificar antes a propriedade __name__
if __name__ == '__main__':
    lista_teste = [1, 2, 3]
    dobro_lista_teste = dobra_lista(lista_teste)
    print(dobro_lista_teste)

# Quando executamos o próprio arquivo o __name__ dele passa a ser __main__
# Já quando esse arquivo está sendo importado, a propriedade __name__ passa a
# ser o próprio nome módulo, nesse caso modulo_aula_53

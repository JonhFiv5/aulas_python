# Em Python tudo é um objeto, inclusive as classes
# Uma metaclasse é uma classe que cria outras
# O type é uma metaclasse, por mais estranho que pareça

# Por isso podemos usar diretamente o type para criar uma classe
# Basta informar: 'NomeClasse', tuple(pai), {dicionario com atributos e metodos}

P = type('P', (), {'nome': None, 'falar_nome': lambda s: print(s.nome)})
# Aqui criamos uma classe que possui o atributo nome e o método falar_nome
pessoa = P()
pessoa.nome = 'Cleiton'
pessoa.falar_nome()


# Esse foi só um exemplo, para criarmos nossa metaclasse precisamos herdar de
# type


class ClasseMeta(type):
    def __new__(mcs, name, bases, namespace):
        # mcs -> A classe em si
        # name -> Nome da classe gerada
        # bases -> Nome dos pais da classe gerada (se houver herança)
        # namespace -> Dicionário com atributos e métodos da classe gerada
        return type.__new__(mcs, name, bases, namespace)


class ClasseGerada(metaclass=ClasseMeta):
    atributo = 10

    def diz_atributo(self):
        print(self.atributo)


# As classes que herdam uma classe gerada também passam pela nossa metaclasse
class FilhaClasseGerada(ClasseGerada):
    pass


filha = FilhaClasseGerada()

# No geral metaclasses não são muito utilizadas,
# mas há alguns usos interessantes
# Por exemplo, se quisermos que o atributo de uma classe não seja sobreescrito
# nas classes filhas:


class Meta(type):

    def __new__(mcs, name, bases, namespace):
        if name != 'Mae':
            if 'atributo_unico' in namespace:
                del namespace['atributo_unico']
        # O bloco acima vai deletar o esse atributo caso seja criado em uma
        # classe filha. Assim quando ela tentar acessar, vai estar acessando o
        # da classe mãe.
        # Podemos fazer várias verificações aqui dentro da metaclasse através
        # dos atributos name, bases e namespace. Assim podemos personalizar a
        # criação de uma classe, gerando até erros caso desejemos que algum
        # comportamento sejo proibido.

        return type.__new__(mcs, name, bases, namespace)


class Mae(metaclass=Meta):
    atributo_unico = 'Definido pela mãe'


class Filha(Mae):
    atributo_unico = 'Definido pela filha'


obj_filha = Filha()
print(obj_filha.atributo_unico)

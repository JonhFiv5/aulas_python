"""Implementando a lista do Python pra entender melhor como funciona"""


class MinhaLista:
    def __init__(self):
        """Cria uma lista vazia ao inicializar uma instância"""
        self.__items = []
        self.__index = 0  # Usada em __next__()

    def adicionar(self, item):
        """Adiciona um item ao fim da lista"""
        self.__items.append(item)

    def __setitem__(self, key, value):
        """Adiciona um item em determinado índice"""
        if key >= len(self.__items):
            # Se o índice for maior que o limite da lista adicionamos no fim
            self.__items.append(value)
        else:
            # Se o índice existir, funciona como uma lista normal
            self.__items[key] = value

    def __getitem__(self, item):
        """Retorna o item de acordo com o índice"""
        return self.__items[item]

    def __delitem__(self, key):
        """Usado para deletar um item de acordo com o index"""
        del self.__items[key]

    # Para implementarmos o protocolo iterator e fazer nossa classe funcionar
    # em laços (for) precisamos implementar dois métodos, o iter e o next

    def __iter__(self):
        # Vai definir em cima do quê queremos iterar, no caso é a própria lista
        return self

    def __next__(self):
        # Vai retornar o próximo valor na iteração
        # Para isso criamos a variável auxiliar index
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            # Após percorrer todos os valores na lista e chegarmos num index
            # vazio (que não existe) levantamos a excessão StopIteration
            # Ela é tratada dentro do for, é o que faz o laço parar
            raise StopIteration

    def __str__(self):
        """Formata para mostrar os valores da lista ao dar um print"""
        return f'{self.__items}'

    def __add__(self, item):
        """Assim podemos usar a soma += como um append"""
        self.__items.append(item)
        return self


lista = MinhaLista()

# Adicionando elementos com o método que criamos
lista.adicionar('queijo')
lista.adicionar('fusca')
lista.adicionar(18)

# Adicionando elementos usando soma, já que sobrescrevemos o __add__
lista += 'lápis'
lista + 'aro'
print(lista)

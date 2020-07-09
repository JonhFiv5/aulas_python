# Classe abstrata é aquela que não vai ser instânciada, servindo apenas como
# superclasse de outras. Uma classe abstrata pode possuir métodos abstratos
# (métodos sem corpo que as subclasses são obrigadas a implementar)
# e métodos concretos (métodos com uma funcionalidade descrita
# já na classe abstrata).

# Antes de tudo precisamos importar pelo menos dois métodos:
# abc -> Abstract Base Class
# ABC -> Uma superclasse de classes abstratas
# abstractmethod -> Um decorador para métodos estáticos

from abc import ABC, abstractmethod


class Pessoa(ABC):
    # Para a classe ser abstrata ela precisa herdar de ABC
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Assim definimos que um método é abstrato.
    # Uma classe só se torna realmente abstrata e não pode ser instânciada
    # se tiver pelo menos um método abstrato
    @abstractmethod
    def falar(self):
        pass


class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self.cpf = cpf

    # Implementando o método abstrato
    def falar(self):
        print('Cliente está falando...')


cli_01 = Cliente('Jurandir', 37, 128492)
cli_01.falar()

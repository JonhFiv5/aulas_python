# Um método estático é uma função como qualquer uma outra,
# mas que por alguma questão de organização ou necessidade
# é colocado dentro da classe.
# Ele não recebe instância(self) nem classe(cls)
# mas pode receber atributos normais, como um função comum.
# Pode ser chamado pela classe e por qualquer instância dela.
from random import randint


class Pet:
    animais_cadastrados = []

    def __init__(self, nome, idade, raca='Vira lata'):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        Pet.animais_cadastrados.append(self)

    # Método de instância
    def dar_banho(self):
        print(f'Você deu banho em {self.nome}.')
        humor = randint(0, 1)
        print('Ele está feliz.' if humor == 1 else 'Ele não gostou.')

    # Método da classe
    @classmethod
    def cadastros(cls):
        print(f'\nTemos {len(cls.animais_cadastrados)} clientes.')
        for animal in cls.animais_cadastrados:
            print()
            print('Nome: ', animal.nome)
            print('Idade: ', animal.idade)
            print('Raça: ', animal.raca, '\n')
            print('-' * 15)

    # Método estático
    @staticmethod
    def ver_info_classe():
        print('-' * 100)
        print(
            'Classe para a criação de pets, recebe o nome(str), a idade(int)'
            ' e a raça(str) do animal.\nPor valor padrão a raça é "vira lata"'
        )
        print('-' * 100)


Pet.ver_info_classe()  # Chamada de método estático

animal_1 = Pet('Rex', 7, 'Pit bull')  # Criação de instância
animal_2 = Pet('Vivi', 3, 'Pastor alemão')
animal_3 = Pet('Safira', 1)

animal_1.dar_banho()  # Chamada de método de instância

Pet.cadastros()  # Chamada de método de classe

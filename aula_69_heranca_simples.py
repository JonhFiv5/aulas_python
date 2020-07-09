# Associação - Usa
# Agregação - Tem
# Composição - É dono
# Herança - É

# Exemplo:
# Um Aluno é uma Pessoa
# Um professor é uma pessoa


class Pessoa:
    # Classe mãe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__  # Pegando o nome da classe

    def bio(self):
        print(f'{self.nome_classe}\nNome: {self.nome}\nIdade: {self.idade}')


class Professor(Pessoa):
    # Classe filha de Pessoa

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)  # Chamada do construtor da classe mãe
        self.salario = salario

    # Sobreescrevendo um método da classe mãe
    def bio(self):
        super().bio()
        print(f'Salário: {self.salario}')


class Aluno(Pessoa):
    # Classe filha de Pessoa

    def __init__(self, nome, idade, serie):
        super().__init__(nome, idade)
        self.serie = serie

    # Sobreescrevendo
    def bio(self):
        super().bio()
        print(f'Série: {self.serie}')


aluno_01 = Aluno('Cleiton', 12, 7)

# Observe que o objeto aluno_01 é uma instância da própria classe e também da
# sua classe mãe (Pessoa), mas como era de se esperar, não é da classe Professor
print(isinstance(aluno_01, Aluno))
print(isinstance(aluno_01, Pessoa))
print(isinstance(aluno_01, Professor))

print('#' * 40)

aluno_01.bio()

professor_01 = Professor('André', 35, 3500)
professor_01.bio()

# Classes em Python são definidas com a
# palavra reservada class e são escritas com letra maiúscula

# Atenção, seguindo as boas práticas cada classe deveria ficar em um módulo
# próprio, separada da criação das instâncias, para isso deveria ser
# realizado um import da classe.
# Por motivos de estudo isso não foi seguido aqui.
from datetime import datetime


class Pessoa:
    # Podemos criar variáveis estáticas (da classe) aqui, antes do __init__
    ano_atual = datetime.today().year

    # A palavra self se refere ao objeto que chama a função, é como um this
    # A função construtora é chamada __init__, após o self definimos quais
    # parâmetros a classe terá

    def __init__(self, nome, idade, com_sono=False):
        self.nome = nome
        self.idade = idade
        self.com_sono = com_sono
        # As variáveis definidas aqui na construtora e colocadas dentro de self
        # Podem ser acessadas por outras funções dessa classe.
        # Entretanto, se criarmos uma variável solta aqui ela não estará
        # acessível
        qualquer_coisa = 'Só sou visível dentro de __init__'

    # Tod0 método possui o self, não é preciso passar ele. É automático.

    def bio(self):
        # print(qualquer_coisa)
        print(
            f'Olá, me chamo {self.nome}'
            f', tenho {self.idade}'
            f' anos e nasci em '
            f'{self.get_ano_nascimento()}'
        )

    def dormir(self, horas):
        # horas só existe no escopo desse método
        if self.com_sono:
            print(f'{self.nome} está com sono e vai dormir {horas} horas.')
        else:
            print(f'{self.nome} não precisa dormir agora.')

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


# Criamos uma instância (um objeto) de uma classe da seguinte forma

# Somos obrigados a passar argumentos se não definimos nenhum valor padrão
pessoa1 = Pessoa('Cleiton', 27)
pessoa1.bio()
pessoa1.dormir(15)
pessoa1.com_sono = True
pessoa1.dormir(15)

# Podemos acessar diretamente uma variável estática
print(Pessoa.ano_atual)

# Objetos também tem acesso a ela
print(pessoa1.ano_atual)

# Alterar o valor de uma variável de classe em uma instância só irá
# mudar o valor naquela instância, permanecendo intacto para a classe
pessoa1.ano_atual = 18
print(pessoa1.ano_atual)  # Alterado para 18
print(Pessoa.ano_atual)  # Continua o mesmo

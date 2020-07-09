# Associação, onde uma classe está relacionada a outra, mas
# uma é independete da outra
# Falando a grosso modo, é salvar uma instância como atributo de outra instância


class Piloto:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self._veiculo = None

    @property
    def veiculo(self):
        return self._veiculo

    @veiculo.setter
    def veiculo(self, carro):
        self._veiculo = carro

    def bio(self):
        print(f'Piloto: {self.nome} \nIdade: {self.idade}')


class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f'Acelerando o {self.marca} {self.modelo}')


piloto_01 = Piloto('Rubinho Massa', 35)
carro_01 = Carro('Chevrolet', 'H-500')
piloto_01.veiculo = carro_01
piloto_01.bio()
piloto_01.veiculo.acelerar()

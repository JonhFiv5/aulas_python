class Animal:
    def __init__(self, especie, alimento):
        self.especie = especie
        self.alimento = alimento

    def comer(self):
        print(f'{self.especie} está comendo {self.alimento}.')


class MeioDeTransporte:
    def __init__(self, capacidade, tipo_terreno):
        self.capacidade = capacidade
        self.tipo_terreno = tipo_terreno
        self.nome_classe = self.__class__.__name__

    def desc(self):
        print(
            f'{self.nome_classe} pode carregar até {self.capacidade} '
            f'pessoas em uma rota {self.tipo_terreno}.'
        )


class Cavalo(Animal, MeioDeTransporte):
    def __init__(self, especie, alimento, capacidade, tipo_terreno, raca):
        # Ao trabalhar com herança múltipla precisamos especificar bem o que
        # estamos acessando, então o super() poderá não funcionar
        Animal.__init__(self, especie, alimento)
        MeioDeTransporte.__init__(self, capacidade, tipo_terreno)
        self.raca = raca

    def relinchar(self):
        print(f'O cavalo {self.raca} está relinchando')


cavalo_01 = Cavalo('Cavalo', 'Cenoura', 2, 'Terrestre', 'Manga larga')

cavalo_01.relinchar()
cavalo_01.comer()
cavalo_01.desc()

# NOTA: Geralmente nós utilizamos herança múltipla onde uma nas superclasses é
# uma mixin (NomeClasseMixin). Essa classe (ainda não considerada abstrata) não
# vai ser usada para gerar instâncias, ela existe apenas para adicionar
# funcionalidades extras para outra classe.

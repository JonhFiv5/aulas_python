# Podemos ter uma herança em vários níveis (o que pode deixar um
# código bem complexo), onde a filha de uma classe pode ser a mãe de outra
# classe. E se há métodos sobreescritos há uma forma de selecionar de qual
# classe queremos que ele seja executado


class Avo:
    def __init__(self):
        ...

    def falar(self):
        print('Avó está falando')


class Filha(Avo):
    def falar(self):
        print('Mãe está falando')


class Neta(Filha):
    def falar(self):
        # Como a herança funciona em cadeia (de cima para baixo), ao acessar a
        # classe super estamos acessando a que está um nível acima dessa, no
        # caso a Filha
        super().falar()

        # Para acessar a classe avô precisamos chamar diretamente o nome dela e
        # passar a instância atual para ela
        Avo.falar(self)

        # Também funcionaria com a filha
        Filha.falar(self)
        # Ou seja, a partir dessa sintaxe podemos acessar o método da classe
        # desejada, não importa em qual nível da herança ela esteja
        # Classe.metodo(self)

        print('Neta está falando')


neta_01 = Neta()

neta_01.falar()

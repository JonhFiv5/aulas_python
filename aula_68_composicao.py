# É o tipo mais forte de relação, onde uma classe não consegue existir
# sem que esteja contida dentro de outra.
# Caso essa classe (instância) "dona" for deletada, todas as instâncias que
# estavam contidas dentro dela também serão apagadas.

# Exemplo de composição, uma classe escola com instâncias de uma classe aluno.
# Se por algum motivo essa escola não existir mais não haverá motivo nem onde
# manter armazenadas as instâncias dos alunos.
# Uma outra analogia seria entre uma tabela de dados e seus registros. Após um
# drop da tabela os registros vão junto.


class Escola:

    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular_aluno(self, nome, idade):
        # Em uma composição, as instâncias da classe dependente são criadas
        # diretamente dentro da classe "dona"
        self.alunos.append(Aluno(nome, idade))

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f'Nome: {aluno.nome}\nIdade: {aluno.idade}\n' + '-' * 30)

    def __del__(self):
        print('Escola deletada!')


class Aluno:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __del__(self):
        # Método executado quando uma instância é deletada
        print(self.nome, 'DELETADO')


escola_sede = Escola('Pedrim Gaspar Mendes')

# Todas as instâncias Aluno foram criados dentro da instância 'escola_sede'
escola_sede.matricular_aluno('Leandro', 15)
escola_sede.matricular_aluno('Dória', 14)
escola_sede.matricular_aluno('Susana', 10)
escola_sede.matricular_aluno('Tiffani', 15)

escola_sede.listar_alunos()

# Observe que ao deletar a instância da escola, todas as instâncias de alunos
# nela também são deletadas junto, disparando o método __del__ e imprimindo na
# saída o nome do aluno que foi deletado.
del escola_sede

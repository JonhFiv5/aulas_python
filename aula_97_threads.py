# Quando executamos um programa executamos um processo
# Até agora os programas que executamos foram na main thread, um único processo

from threading import Thread
from time import sleep

from threading import Lock

# Exemplo 1 ------------------------------------------------------------
"""
class MinhaThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MinhaThread('Thread 1 executada!', 3)
t1.start()  # Iniciamos o método run()

# Threads só podem ser executadas uma vez

t2 = MinhaThread('Thread 2 executada!', 3)
t2.start()

for i in range(10):
    print(i)
    sleep(1)
"""

# Exemplo 2 ------------------------------------------------------------
"""
def cozinhar(alimento, tempo_preparo):
    sleep(tempo_preparo)
    print(f'{alimento} já ficou pronto!')


# Em um código comum cada tarefa seria executada após o fim da anterior, já com
# threads todas começam ao mesmo tempo. O que é bem mais rápido.

# Executa em 8 segundos (aproximadamente)
t1 = Thread(target=cozinhar, args=('Arroz', 4))
t1.start()

t2 = Thread(target=cozinhar, args=('Feijão', 8))
t2.start()

t3 = Thread(target=cozinhar, args=('Bife', 2))
t3.start()

# Executa em 14 segundos (aproximadamente)
# cozinhar('Arroz', 4)
# cozinhar('Feijão', 8)
# cozinhar('Bife', 2)

# Código executado na main thread
print('Acendeu a primeira boca do fogão...')
print('Acendeu a segunda boca do fogão...')
print('Acendeu a terceira boca do fogão...')

# Na main thread podemos saber quando uma thread secundária terminou de
# executar pela função is_alive()
while t1.is_alive() or t2.is_alive() or t3.is_alive():
    sleep(1)
print('Almoço pronto!')

# Também podemos fazer a thread principal esperar por outra usando:
# nome_thread.join()
"""

# Exemplo 3 ------------------------------------------------------------
# Como threads são assíncronas, podem haver problemas com o nosso código


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()  # Classe importada de threading

    def comprar(self, quantidade):
        # O método acquire() vai trancar o método comprar
        # depois de uma thread entrar nele
        self.lock.acquire()

        if self.estoque < quantidade:
            print(f'Não temos ingressos suficientes.')

            # Colocamos o método release() em pontos de saída do nosso método
            # Para assim que uma thread sair do método, liberar passagem para
            # que outra possa entrar.
            # Assim uma thread irá acessar o método por vez
            self.lock.release()
            return

        sleep(1)
        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} no estoque.')

        self.lock.release()


ingresso = Ingressos(10)

for i in range(1, 15):
    t1 = Thread(target=ingresso.comprar, args=(i, ))
    t1.start()

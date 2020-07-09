# Faça uma lista de tarefas com as seguintes opções:
# * Adicionar uma tarefa
# * Listar tarefas
# * Opção de desfazer (a cada vez que chamamos, defaz a última ação)
# * Opção de refazer (a cada vez que chamamos, refaz a última ação)

lista_tarefas = []
tarefas_temp = []
last_actions = []
while True:
    opcao = str(
        input(
            '[1] Nova tarefa\n'
            '[2] Listar tarefas\n'
            '[3] Desfazer ação\n'
            '[4] Refazer ação\n'
            '[0] Sair\n'
        )
    )

    # [0] Sair
    if opcao == '0':
        print('Adios')
        break

    # [1] Nova tarefa
    elif opcao == '1':
        last_actions.append(1)
        lista_tarefas.append(input('Insira uma nova tarefa: '))

    # [2] Listar tarefas
    elif opcao == '2':
        if len(lista_tarefas) > 0:
            for tarefa in lista_tarefas:
                print(f'*{tarefa}')
        else:
            print('Lista vazia')

    # [3] Desfazer ação
    elif opcao == '3':
        if len(lista_tarefas) > 0:
            tarefas_temp.append(lista_tarefas.pop())
        else:
            print("Não é possível retroceder além desse ponto.")

    # [4] Refazer ação
    elif opcao == '4':
        if len(tarefas_temp) > 0:
            lista_tarefas.append(tarefas_temp.pop())
        else:
            print("Não é possível avançar além desse ponto.")

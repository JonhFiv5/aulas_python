# Sistema de perguntas e respostas com múltipla escolha
from time import sleep

dicio_perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': 4,
            'b': 3,
            'c': 2,
            'd': 7,
        },
        'resposta_certa': 'a',
    },

    'Pergunta 2': {
        'pergunta': 'Quem foi D. Pedro II?',
        'respostas': {
            'a': 'Presidente de Portugal',
            'b': 'Rei da Espanha',
            'c': 'Primeiro Ministro',
            'd': 'Imperador do Brasil',
        },
        'resposta_certa': 'd',
    },

    'Pergunta 3': {
        'pergunta': 'Qual o maior animal terrestre atualmente?',
        'respostas': {
            'a': 'Elefante',
            'b': 'Cavalo',
            'c': 'Rinoceronte',
            'd': 'Baleia',
        },
        'resposta_certa': 'a',
    },

    'Pergunta 4': {
        'pergunta': 'Qual é o resultado de vermelho misturado com amarelo?',
        'respostas': {
            'a': 'Marrom',
            'b': 'Laranja',
            'c': 'Roxo',
            'd': 'Rosa',
        },
        'resposta_certa': 'b',
    }
}

pontuacao = 0

for chave_p, valor_p in dicio_perguntas.items():
    print(f'{chave_p}: {valor_p["pergunta"]}')

    for chave_r, valor_r in valor_p['respostas'].items():
        print(f'({chave_r}): {valor_r}')

    resposta_usuario = input('Escolha a alternativa correta: ')
    if resposta_usuario == valor_p['resposta_certa']:
        print('Você acertou!')
        pontuacao += 1
    else:
        print('Errou...')
    print('-' * 70)
    sleep(1)

print('Sua pontuação final foi: ', pontuacao)

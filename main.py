Perguntas = {
    'Pergunta 1': {
        'Pergunta': 'Qual o Tamanho do Universo?',
        'Respostas':{'A': '28 Milhões de anos','B': '156 bilhões de anos luz'},
        'RespostaCert': 'A',

    }
}
RespostaCert = 0
for Pkey, Rkey in Perguntas.items():
    print(f'{Pkey}: {Rkey["Pergunta"]}')

    for rk, rv in Rkey['Respostas'].items():
        print(f'[{rk}]: {rv}')

RespostaUser = input('[R]:')

if RespostaUser == Rkey['RespostaCert']:
    print('Exatamente!')
    RespostaCert += 1
else:
    print('Não! na verdade essa é só uma estimatia de seu tamanho atual')

print()

QtdPerguntas = len(Perguntas)
Porcentagem = RespostaCert / QtdPerguntas * 100

print(f'Acertou {RespostaCert} Respostas')
print(f'Sua Porcentagem de acerto foi de {Porcentagem}%.')

print()
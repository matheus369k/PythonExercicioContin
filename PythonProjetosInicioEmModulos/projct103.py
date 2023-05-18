print('-'*17, 'FICHA DO JOGADOR', '-'*17)


def ficha(a, b):
    if a == '':
        a = '<descomhecido>'
    if b not in '1234567890 ' or b in '':
        b = 0
    print(f'O jogador {a} fez {b} gol(s) no campeonato.')


ficha(a=str(input('Nome do Jogador: ')), b=str(input('Numero de Gols: ')))


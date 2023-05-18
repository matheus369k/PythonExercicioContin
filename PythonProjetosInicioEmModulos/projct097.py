while True:
    def escreva(digite):
        com = len(digite) + 4
        print('\033[;33m-' * com)
        print(f'\033[;32m: {digite} :')
        print('\033[;33m-' * com)


    #PROGRAMA PRINCIPAL
    escreva(digite=str(input('\033[;33mEscreva uma Frase ou Palavra: ')))
    con = str(input('Quer continuar? [S/N]: '))
    while con not in 'NSns':
        con = str(input('Quer continuar? [S/N]: '))
    if con in 'nN':
        break
def cust(c, t):
    tan = len(t)
    print(f'\033[7;3{c}m~' * tan)
    print(t)
    print(f'\033[7;3{c}m~' * tan)

while True:
    cust(2, ':  SISTEMA DE AJUDA DO PYHELP  :')
    ajuda = str(input('\033[mFunção ou Biblioteca (FIM sair)>'))
    if ajuda.upper() == 'FIM':
        break
    else:
        cust(6, f":  Acessando o manual de comando '{ajuda}'  :")
        print('\033[m\033[7m', end='')
        help(ajuda)



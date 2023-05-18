def voto(ano):
    from datetime import datetime
    global idade
    idade = datetime.today().year - ano
    if 65 > idade >= 18:
        r = '\033[;31mVOTO OBRIGATORIA!'
    elif idade < 16:
        r = '\033[;31mNAO VOTA!'
    else:
        r = '\033[;32mVOTO OPCIONAL!'
    return r


#PROGAMA PRINCIPAL
print('\033[;36m-' * 19, '\033[;31mVoto', '\033[;36m-' * 19)
v = voto(ano=int(input('\033[;33mA.D.NACIMENTO: ')))
print(f'\033[;33mCom {idade} anos:{v}.')

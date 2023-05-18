
def metade(num=0,sf=False):
    num /= 2
    if sf == True:
        return moeda(num, 'R$', sf=True)
    else:
        return num


def dobro(num=0,sf=False):
    num *= 2
    if sf == True:
        return moeda(num, 'R$', sf=True)
    else:
        return num


def aumento(num=0, a=10, sf=False):
    num += (num * a) / 100
    if sf == True:
        return moeda(num, 'R$', sf=True)
    else:
        return num


def reduz(num=0, r=13, sf=False):
    num -= (num * r) / 100
    if sf == True:
        return moeda(num, 'R$', sf=True)
    else:
        return num


def moeda(num=0, moeda='R$', sf=False):
    if sf == True:
        num = f'{moeda}{num:.2f}'.replace('.', ',')
    return num


def l(tan=30):
    print('\033[;31m-\033[;32m' * tan)


def resumo(num=0, a=80, r=35):
    l()
    print('       RESUMO DO VALOR        ')
    l()
    print(f'Preço analizado:{moeda(num, sf=True):>14}')
    print(f'Dobro do preço:{moeda(dobro(num, sf=True)):>15}')
    print(f'Metade do preço:{moeda(metade(num, sf=True)):>14}')
    print(f'{a}% de aumento:{moeda(aumento(num, a=a, sf=True)):>15}')
    print(f'{r}% de redução:{moeda(reduz(num, r=r, sf=True)):>15}')
    l()

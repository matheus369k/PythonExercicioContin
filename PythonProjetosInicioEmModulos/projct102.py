print('-'*20,'Fatorial','-'*20)


def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    a = 1
    for c in range(num, 0, -1):
        a *= c
        if show == True:
            if c > 1:
                print(f'{c}',end=' X ')
            if c == 1:
                print(f'{c} = ',end='')
    return a


#PROGAMA PRINCIPAL
print(fatorial(5,True))
help(fatorial)


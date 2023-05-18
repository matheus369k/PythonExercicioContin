from random import randint
from time import sleep
def sorteia (list):
    for c in range(1,6):
        list.append(randint(1,10))
    print(f'\033[;33mSorteado {len(list)} valores da lista', end='')
    for p in range(0, 6):
        sleep(0.6)
        print('.', end='')
    for c in list:
        sleep(0.6)
        print(c, end=' ')
    sleep(1)
    print('\033[;32mPRONTO!')
    sleep(1.3)


def somapar():
    print('\033[;33mSomando os valores pares da lista ', end='')
    to = 0
    for t in  list:
        if t % 2 == 0:
            sleep(0.6)
            print('\033[;32m',t, end=' ')
            to += t
        else:
            sleep(0.6)
            print('\033[;31m',t, end=' ')
    print(f'\033[;33m, temos: \033[;32m',end='')
    sleep(2)
    print(f'{to}.')

list = list()
sorteia(list)
somapar()
from time import sleep
def l():
    print('\033[;33m-'*20, '\033[;32mLista', '\033[;33m-'*20)
def contador(*num):
    print('\033[;32mAnalizando os valores passador', end='')
    for p in range(0, 5):
        sleep(0.7)
        print('.', end='')
    print()
    for c in num:
        print(c, end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(0.5)
    if len(num) != 0:
        print(f'O maior valor informado foi {max(num)} nesta lista.')
    else:
        print('\033[;31mNAO EXISTE!\033[;32m maior valor nesta lista.')
    sleep(0.5)
l()
contador(2, 9, 4, 5, 7, 1)
l()
contador(4, 7, 0)
l()
contador(1, 2)
l()
contador(6)
l()
contador()
print('\033[;33m-'*14, '\033[;31mPROGAMA ENCERRADO', '\033[;33m-'*14)

from time import sleep
def cont(a, b, c):
    print('\033[;33m-'*20,' \033[;32mContagem ','\033[;33m-'*20)
    if c < 0:
        c -=(c+c)
    print(f'\033[;32m\nContagem de {a} a {b} de {c} em {c}.\033[;36m')
    if c == 0 :
        c = 1
    if a > b:
        if c > 0:
            c -= c+c
        b -= 1
    if a < b:
        b += 1
    conti = 0
    for t in range(a, b ,c):
        conti += 1
        sleep(0.5)
        print(f'{t}',end=' ')
        if conti > 12:
            print('\n',end='')
            conti = 0
    print('\033[;31mFIM!')


cont(a=1, b=10, c=1)
cont(a=10, b=0, c=2)
print('\033[;33m-'*20,'\033[;32mPersonalize','\033[;33m-'*20)
print('\033[;32mAgora e sua vez personalize sua contagem!')
while True:
    cont(a=int(input('Inicío: ')),b=int(input('Fim: ')),c=int(input('Passo: ')))
    con = str(input('\033[;33mQuer personalizar outra? [S/N]: '))[0]
    while con not in 'SNsn':
        print('\033[;31mRESPOSTA INVALIDA.')
        con = str(input('\033[;33mQuer personalizar outra? [S/N: '))[0]
    if con in 'nN':
        break
    print('\033[;33m-' * 20, '\033[;32mPersonalize outra', '\033[;33m-' * 20)
print('\033[;33m-'*25,'\033[;31mFIM','\033[;33m-'*25)
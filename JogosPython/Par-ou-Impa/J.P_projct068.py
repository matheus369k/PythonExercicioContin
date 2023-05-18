from pygame import mixer
from time import sleep
from random import randint
cor = '\033[m'
print(f'{cor}%=%'*10,'\n     \033[0;35mJogo de Par ou Impar.')
print(f'{cor}%=%'*10)
num = d = v = t = 0
g = 5
r = ''
mixer.init()
while True:
    num = int(input('\n\033[0;33mESCOLHA UM NUMERO: '))
    pc = randint(0,11)
    print(f'{cor}%=%'*10)
    pla = str(input('\n\033[0;33mPAR OU INPAR P/I:')).upper().strip()[0]
    sleep(1)
    while pla not in 'PI':
        pla = str(input('PAR OU IMPAR P/I:')).upper().strip()[0]
    t = num + pc
    if t/2%1 == 0:
        r = 'PAR'
    elif t/2%1 != 0:
        r = 'IMPAR'
    if pla == r[0]:
        mixer.music.load('You Win (Street Fighter) - Sound Effect.mp3')
        mixer.music.play()
        print(f'{cor}%=%'*10,'\n\033[0;32mCONGRATOLATION!!\n')
        print('YOU WIN!!')
        v += 1
    elif pla != r[0]:
        mixer.music.load('Game Over sound effect.mp3')
        mixer.music.play()
        print(f'{cor}%=%'*10,'\n\033[0;31mGAME OVER!!!!')
        d += 1
        sleep(3)
        if v == 0:
            mixer.music.load('Risada Demoníaca [Demonic Laugh].mp3')
            mixer.music.play()
            print('\n\033[0;31mSEM SORTE!!!!')
            print(f'{cor}%=%' * 10)
            sleep(5)
            input('\033[mClick......')
            break
        else:
            break
    sleep(2.7)
    mixer.music.load('win01.wav')
    mixer.music.play()
    print(f'{cor}%=%'*10,f'\n\033[0;34m{r} VENCEU!!')
    print(f'\033[0;34mPC ESCOLHEU: {pc}\nVOCE ESCOLHE: {num}\nSOMA E: {t}.')
    print(f'{cor}%=%'*10)
    if v == g:
        mixer.music.load('Efeitos Sonoros - Anjos.mp3')
        mixer.music.play()
        print('\n\033[mVOCE E UMA DIVINDADE NESSE GAME!!!!!!!!')
        g += 5
        print(f'{cor}%=%'*10)
        input('\033[mClick......')
print(f'\033[0;36mVOCE GANHOU {v}X SEGUIDAS!!!')
print('\033[m%=%'*10)




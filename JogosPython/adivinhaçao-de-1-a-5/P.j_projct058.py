from random import randint
from time import sleep
from pygame import mixer
c = 1
p = j = 0
c = randint(1,11)
while p != c:
    print(' ' * 40, '\033[0;34m( ADIVINHAÇAO )')
    print('\33[0;31m( PC.VS.PLAYER )')
    print('==='*10)
    sleep(0.5)
    print('\033[0;33mPC PENSANDO', end='')
    for h in range(0,5):
        sleep(0.2)
        print('.', end='')
    mixer.init()
    mixer.music.load('win01.wav')
    mixer.music.play()
    print('\nPRONTO!!!!')
    print('==='*10)
    sleep(0.5)
    p = int(input('\033[0;36mQUE NUMERO ACHA QUE PENSEI? '))
    sleep(0.5)
    mixer.music.load('win01.wav')
    mixer.music.play()
    print('\033[0;33mSERA...')
    sleep(0.5)
    print('SERA QUE ACERTOU.')
    sleep(2)
    print('==='*10)
    if p == c:
        mixer.music.load('You Win (Street Fighter) - Sound Effect.mp3')
        mixer.music.play()
        print('\033[0;32mPARABENS!!!')
        sleep(1)
        print('VOCE GANHOU!!!')
    elif p > c:
        mixer.music.load('Game Over sound effect.mp3')
        mixer.music.play()
        sleep(1)
        print('\033[0;31mMENOS -')
    elif p < c:
        mixer.music.load('Game Over sound effect.mp3')
        mixer.music.play()
        sleep(1)
        print('\033[0;31mMAIS +')
    j +=1
    sleep(2)
if j < 3:
    mixer.music.load('win01.wav')
    mixer.music.play()
    print('\033[0;32mVOCE E MUITO SORTUDO!!!')
    print('VOCE GANHOU COM SO {} DERROTAS'.format(j-1))
else:
    mixer.music.load('over01.wav')
    mixer.music.play()
    print('\033[0;33mVOCE E AZARADO...')
    print('VOCE SO GANHOU DEPOIS DE {} DERROTAS.'.format(j-1))
input('SAIR')
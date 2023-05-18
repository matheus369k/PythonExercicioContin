def jogo_adivinhe():
    from random import randint
    from time import sleep
    from pygame import mixer,event
    print(' '*10,'\033[0;34m-=-'*25)
    print(' '*10,'<==        Adivinhe o Nomero Escolhido Pelo Computador de 0 A 5!!       ==>')
    print(' '*10,'-=-'*25)
    n = int(input('\033[0;32mDigite o Numero Aqui: '))
    n_c = randint(0,5)
    print('\033[0;33mPROCESSANDO.....')
    sleep(2)
    if n == n_c:
        mixer.init()
        mixer.music.load('win01.wav')
        mixer.music.play()
        print('\033[0;32m-=-'*17)
        print('-=-'*17)
        print('-=-'*17)
        print('-=-'*6,'\033[0;33m<PARABENS!!!>','\033[0;32m-=-'*6)
        print('-=-'*6,'\033[0;33m<VOCE ACERTOU!!>','\033[0;32m-=-'*5)
        print('-=-'*17)
        print('-=-'*17)
        print('-=-'*17)
    else:
        mixer.init()
        mixer.music.load('over01.wav')
        mixer.music.play()
        print('\033[0;33m-=-'*15)
        print('-=-'*15)
        print('-=-'*15)
        print('-=-'*4,'\033[0;34m<VOCE ERROU!!!!>','\033[0;33m-=-'*5)
        print('-=-'*3,'\033[0;34m<BOA SORTE NA PROXIMA...>','\033[0;33m-=-'*3)
        print('-=-'*15)
        print('-=-'*15)
        print('-=-'*15)
        print('-=-'*2,'\033[0;36m<O Computador Escolheu O Numero {}.>\033[0;33m-=-'.format(n_c))
        print('-=-'*15)
print(jogo_adivinhe())
while True:
    escolha = str(input('\033[0;34mQuer tentar  outra vez \033[0;33mS/sim\033[m ou \033[0;31mN/nao\033[m ? ')).lower()
    if escolha == 's':
        jogo_adivinhe()
    elif escolha == 'n':
        exit()
    else:
        print('\033[0;31mSO ESCREVA S PARA SIM OU N PARA NAO')
else:
    exit()

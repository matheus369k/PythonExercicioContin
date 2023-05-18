from time import sleep
from pygame import mixer
print('\033[0;36m=-='*8)
print('<CONTAGEM REGRECIVA!!!!>')
print('=-='*8)
mixer.init()
mixer.music.load('CONTAGEM REGRESSIVA COM SOM.mp3')
mixer.music.play()
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\033[0;34mFELIZ ANO NOVO!!!!')
print('=-='*9)
mixer.init()
mixer.music.load('Som De Fogos de artifício Audio Estouros de fogos.mp3')
mixer.music.play()
sleep(22)





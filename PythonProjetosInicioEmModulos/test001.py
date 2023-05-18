'''''''''
def test_print ():
    n1 = int(input('digite um valor:'))
    n2 = int(input('digite outro valor:'))
    s = n1 + n2
    print('soma entre {} e {} vale {}'.format(n1, n2, s))

def test_type():
    n = (input('digite um valor'))
    print(type(n))

def operaçoes ():
    print('\nOs operadores do python sao:\n( + ) para adiçao.\n( - )para subtraçao.\n( * )para multiplicaçao.\n( / )para divisao.')
    print('( ** ) para potencia.\n( ** 0.5 )raiz quadrada.\n( // ) para divisao inteira.\n( % )para resto da divisao.')
    print('\nordem de precedencia:\n1 = ().\n2 = **.\n3 = *, /, //, %.\n4 = +, -.')

print('1 = test_print.\n2 = test_type.\n3 = operaçoes_re-lembrar.')
escolha = input('Escolha:')
if escolha == '1':
    test_print()
if escolha =='2':
    test_type()
if escolha == '3':
    operaçoes()
'''''''''''
'''
import math
print((3**0.5)/2)
print(math.cos(30))
'''
''''
from math import sin,radians,cos,tan
angulo = float(input('digite o angulo desejado: '))
seno = sin(radians(angulo))
print('O angulo {}º, tem Seno  {:.3f}.'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O angulo {}º, tem o Cosseno {:.3f}.'.format(angulo,cosseno))
tangete = tan(radians(angulo))
print('O angulo {}º, tem a Tangent {:.3f}'.format(angulo,tangete))
'''''''''
''''
from random import choice
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))
'''''
''''
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 =  str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A orda da lista sera......')
print(lista)
'''''
'''
from pygame import mixer,event
mixer.init()
mixer.music.load('RpProjct.mp3')
mixer.music.play()
parar = input('Para?')
'''
'''''''''
varial = 'Curso em video de python'
print(varial[9:14],varial[15:17],varial[18:26])
print(varial[9:26:2])
print(varial[:5])
print(varial[18:])
print(varial[9::3])
print(len(varial))
print(varial.count('o',0,14))
print(varial.find('android'))
print('Curso' in varial)
varial.replace('python','android')
print(varial.upper())
print(varial.lower())
print(varial.capitalize())
print(varial.title())
new = '   Aprenda Python  '
print(new)
print(new.strip())
print(new.rstrip())
print(new.lstrip())
print(varial.split())
varial1 = varial.split()
print('-'.join(varial1))
'''''''
''''''''''''
nome = str(input('DIGITE SEU NOME COMPLETO AQUI: ')).strip()
print('analizando seu nome....')
print('seu nome maiusculon é {}'.format(nome.upper()))
print('seu nome minusculo é {}'.format(nome.lower()))
print('seu  nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('seu primeiro nome e {} e ele tem {} letras'.format(separa[0],len(separa[0])))
'''''''''
'''''''''
num = int(input('imforme o numerio: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o numero{}'.format(num))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))
'''''''''''
''''''''''
cid = str(input('em que cidade vc naceu?')).strip()
print(cid[0:5].title() == 'Santo')
'''''
'''''''''
nome = str(input('quanl e seu nome completo?: ')).strip().lower().title()
print('seu nome tem Silva? {}'.format('Silva' in nome))
'''''
'''''''''
frase = str(input('digite uma frase: ')).upper().strip()
print ('a letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('a primeira letra A apareceu na posiçao {}'.format(frase.find('A')+1))
print('a ultima letra A apareceu na posiçao {}'.format(frase.rfind('A')+1))
'''
'''''''''
nome = str(input('digite seu nome completo: ')).strip()
nome1 = nome.split()
print('seu primeiro nome e {}.'.format(nome1[0]))
print('seu ultimo nome e {}.'.format(nome1[len(nome1)-1]))
'''
''''''''''
nome = str(input('qual e seu nome?'))
if nome == 'matheus':
    print('que nome lindo vc tem!')
else:
    print('seu nome e tão normal.')
print('bom dia {}'.format(nome))
'''''
'''''''''
n1 = float(input('Digite a primeira nota: '))
n2 =float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('Parabens!!')
else:
    print('Estude mais.')
'''
'''''''''''''''''
print('\033[0;30;41mhello word')
print('\033[4;33;44mhello word')
print('\033[1;35;43mhello word')
print('\033[30;42mhelo word')
print('\033[mhello word')
print('\033[7;30mhello word')
'''''
t = 1
f = 1
f += t
f -= t
print(t)
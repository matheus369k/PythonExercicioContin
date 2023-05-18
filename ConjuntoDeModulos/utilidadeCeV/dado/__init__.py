
def leiaDinheiro(num):
    """
    -> Validar um valor monetario (ATENÇÃO: Aceita valores com virgula.)
    :param num: Valor a ser validado.
    :return: numero valido.
    """
    ok = False
    while True:
        t = str(input(num))
        t = t.strip()
        if t.isnumeric() or len(t) != t.count('.') != 0 or len(t) != t.count(',') != 0:
            t = t.replace(',', '.')
            t = float(t)
            break
        else:
            ok = True
            print(f'\033[;31mERRO! [\033[m {t} \033[;31m] e um preço invalido.')
    return t


def leiaInt(n):
    """
    -> Para validar se um numero e inteiro ou não.
    :param n: Numero a ser validado.
    :return: retonar o numero valido.
    """
    while True:
        try:
            i = int(input(n))
            return i
        except (ValueError):
            print(f'\033[;31mERRO! Por favor digite um numero inteiro Valido.\033[;32m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[;31mO usuario escolheu ignorar essa opçao.\033[;32m')
            return 0
        else:
            break

def leiaFloat(num):
    """
    -> Para validar se e float ou nao.
    :param num: Numero  a ser valadado.
    :return: retornar o numero que foi validado.
    """
    while True:
        while True:
            try:
                f = float(input(num))
                return f
            except (ValueError):
                print(f'\033[;31mERRO! Por favor digite um numero real Valido.\033[;32m')
                continue
            except (KeyboardInterrupt):
                print('\n\033[;31mO usuario escolheu ignorar essa opçao.\033[;32m')
                return 0
            else:
                break


def Cadrastar(no, i):
    """
    -> Criar e editar registros.
    :param no: Nome de um individuo.
    :param i: Idade de um induviduo
    :return: retorna o nome do individuo
    """
    i = str(i)
    try:
        arquivo = open('r.text', 'r')
        registro = arquivo.readlines()
        arquivo = open('r.text', 'w+')
        registro.append(no[:])
        registro.append(i[:])
        arquivo.writelines(registro[:])
        registro.clear()
        arquivo.close()
    except FileNotFoundError:
        registro = []
        arquivo = open('r.text', 'w+')
        registro.append(no[:])
        registro.append(i[:])
        arquivo.writelines(registro[:])
        registro.clear()
        arquivo.close()
    except:
        print('ERRO ao tentar criar um novo cadrastro')
    finally:
        arquivo.close()
    return no



def ler():
    """
    -> Ler arquivos de texto com numeros
    :return: Sem retorno
    """
    try:
        a = n = tan = 0
        arquivo = open('r.text', 'r')
        read = arquivo.readlines()
        h = 1
        t = 5 - len(str(h))
        print(f'{"N."}{"NOME":>8}{"IDADE":>40}')
        print('\033[;31m-\033[;32m' * 50)
        print(f'{h}',' ' * t, end='')
        for row in range(0, len(read[0])):
            if read[0][row].isnumeric() and a == -1:
                tan = 40 - tan
                print(' ' * tan, end='')
                tan = 0
            if read[0][row].isalpha() and n == -1:
                h += 1
                t = 5 - len(str(h))
                print(f'\n{h}',' ' * t, end='')
            if read[0][row].isalpha():
                print(read[0][row], end='')
                tan += 1
                a = -1
            else:
                a += 1
            if read[0][row].isnumeric():
                print(read[0][row], end='')
                n = -1
            else:
                n += 1
        print()
    except:
        print('ERRO ao tentar ler o arquivo')
    finally:
        arquivo.close()


def time(p=5):
    """
    -> Criar animaçao de pontos
    :param p: quantidade de pontos animados
    :return: Nao ha
    """
    from time import sleep
    for c in range(0,p):
        sleep(0.5)
        print('.',end='')


def cadrastar_s(no='Desconhecido',i=0):
    h = 0
    try:
        arquivo = open('r.text', 'at')
    except:
        print('ERRO ao tentar abrir')
    else:
        try:
            h += 1
            arquivo.write(f'{no};{i}\n')
        except:
            print('ERRO ao tentar cadrastar nova pessoa.')
        else:
            print(f'Novo cradrastro de {no}.')
    finally:
        arquivo.close()


def ler_s():
    try:
        arquivo = open('r.text', 'rt')
    except:
        print('arquivo não encontrado')
    else:
        print(arquivo.read())
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:<5} ANOS')
    finally:
        arquivo.close()

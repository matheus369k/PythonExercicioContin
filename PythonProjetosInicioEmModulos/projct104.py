print('-'*20,'Numero Inteiro','-'*20)
def leiaInt(n):
    while True:
        t = input(n)
        if len(t) != 0:
            if t[0] in '1234567890' and t not in '.':
                break
            else:
                print('\033[;31mERRO! Digite um  número inteiro válido.\033[m')
        else:
                print('\033[;31mERRO! Digite um  número inteiro válido.\033[m')
    return t


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um numero inteiro: ')
print(f'Voce acabou de digitar o número {n}.')
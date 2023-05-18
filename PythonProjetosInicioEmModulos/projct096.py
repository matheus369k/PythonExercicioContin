def area(l, c):
    area = l * c
    print(f'A área de um terreno \033[;32m{l}\033[;33m X \033[;32m{c}\033[;33m é de \033[;32m{area:.1f}m².')

#Programa principal
print('\033[;32mControle de Terrenos')
print('\033[;36m-\033[m'*22)
l = float(input('\033[;33mLARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)



from ConjuntoDeModulos.finaçasevoluçao import moeda

num = float(input('Digite o preço: R$'))
print(f'A metado de R${num} e R${moeda.metade(num)}')
print(f'O Dobro de R${num} e R${moeda.dobro(num)}')
print(f'Aumento de 10%, temos R${moeda.aumento(num, 10)}')
print(f'Reduzindo 13%, temos R${moeda.reduz(num, 13)}')

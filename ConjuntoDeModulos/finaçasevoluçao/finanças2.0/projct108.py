from ConjuntoDeModulos.finaçasevoluçao import moeda

num = float(input('Digite o preço: R$'))
print(f'A metado de {moeda.moeda(num, sf=True)} e {moeda.moeda(moeda.metade(num=num, sf=True))}')
print(f'O Dobro de {moeda.moeda(num, sf=True)} e {moeda.moeda(moeda.dobro(num=num, sf=True))}')
print(f'Aumento de 10%, temos {moeda.moeda(moeda.aumento(num=num, a=10, sf=True))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.reduz(num=num, r=13, sf=True))}')

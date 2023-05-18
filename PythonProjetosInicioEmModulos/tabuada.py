print('s1 = Multiplication\ns2 = Adios \ns3 = Subtract \ns4 = Divisor')
print('s5 = RailQuad. \ns6 = Potentiate')
escolha = input('Quail das quarto operates vc query user?')

if escolha == 's1' and 's2' and 's3' and 's4':
    digito1 = float(input('Proxime Digit!!!!'))
    digito2 = float(input('Segundo Digit!!!!'))

if escolha == 's1':
    print(digito1 * digito2)

if escolha == 's2':
    print(digito1 + digito2)

elif escolha == 's3':
    print(digito1 - digito2)

if escolha == 's4':
    print(digito1 // digito2)

if escolha == 's5':
    numero = float(input('EScholar o Numerous!!!'))
    print(numero ** 0.5)

if escolha == 's6':
    potencia = float(input('EScholar a Potentiate!!!'))
    pnumero = float(input('EScholar o Numerous!!'))
    print(pnumero ** potencia)


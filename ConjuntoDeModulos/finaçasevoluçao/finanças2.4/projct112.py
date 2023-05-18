
from ConjuntoDeModulos.utilidadeCeV import moeda,dado

num = dado.leiaDinheiro('\033[;33mDigite o preço: R$')
moeda.resumo(num, a=80, r=35)

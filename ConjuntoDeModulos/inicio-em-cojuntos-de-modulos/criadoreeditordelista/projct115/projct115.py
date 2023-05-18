
while True:
    try:
        from ConjuntoDeModulos.utilidadeCeV import dado, moeda
    # Menu do sistema
        moeda.l(50)
        print('\033[;33mMENU PRINCIPAL'.center(50))
        print('\033[;32m')
        print('3 - Ver pessoas cadastradas.\n4 - Cadastrar nova pesoa.\n5 - Sair do Sistema')
        print('\033[;32m')
    # Validar opção do menu
        es = str(input('Sua Opção: '))
        while es not in '3 4 5' :
            print('\033[;31mERRO! Opçao invalida\033[;32m')
            es = str(input('Sua Opção: '))
        moeda.l(50)
    # Criar lista
        if es == '3':
            print('\033[;33mOPÇAO 3: PESSOAS CADASTRADAS'.center(50))
            print('\033[;32m')
            dado.ler()
    # Ler lista
        if es == '4':
            print('\033[;33mOPÇAO 4: Registrar\033[;32m'.center(50))
            print()
            n = dado.Cadrastar(no=str(input('NOME: ')).title(), i=dado.leiaInt('IDADE: '))
            print(f'Novo registro!\n{n} adicionado(a).')
    # Saida normal
        if es == '5':
            print('\033[;33mOPÇAO 5: Sair'.center(50))
            print()
            print('\033[31mSAINDO DO SISTEMA',end='')
            dado.time(8)
            print()
            moeda.l(50)
            break
    # Saida forçada
    except KeyboardInterrupt:
        print('\033[;31mUsuario preferiu encerrar o progama forçadamente.')
        print('\033[31mSAINDO DO SISTEMA',end='')
        dado.time(8)
        print()
        moeda.l(50)
        break
    # Não ha lista
    except FileNotFoundError:
        print('\033[;31mNÃO HA LISTA CRIADA!'.center(50))

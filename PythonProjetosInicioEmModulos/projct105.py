print('-'*26, 'Dicionario De Medias', '-'*26)


def notas(* num, sit):
    """
    -> Função para analizar notas e sítuações de varios alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a sítuação.
    :return: Dicionário com várias informações sobre a situação da túrma.
    """
    dict = {}
    dict['TOTAL'] = len(num)
    dict['MAIOR'] = max(num)
    dict['MENOR'] = min(num)
    dict['MEDIA'] = sum(num)/len(num)
    if sit == True:
        if dict['MEDIA'] >= 7:
            dict['SITUAÇAO'] = 'BOA'
        elif 5 < dict['MEDIA'] < 7:
            dict['SITUAÇAO'] = 'RAZOAVEL'
        elif dict['MEDIA'] < 5:
            dict['SITUAÇAO'] = 'RUIM'
    return dict


# PROGRAMA PRINCIPAL
resp = notas(9.5, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)

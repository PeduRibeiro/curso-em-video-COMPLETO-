def notas(*n, sit=True):
    """
    -> Função para analisar notas e situacao de alunos.
    :param n: uma ou mais notas dos alunos (aceita varias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situção.
    :return: Dicionario com varias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

# Programa principal
resp = notas(5.5, 2.5, 8.5)
print(resp)

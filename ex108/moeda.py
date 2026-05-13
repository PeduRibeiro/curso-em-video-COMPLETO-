def aumentar(preço = 0, taxa = 0):
    res = preço + (preço * taxa/ 100)
    return res


def diminuir(preço = 0, taxa = 0):
    res = preço - (preço * taxa/100)
    return res


def metade(preço = 0):
    return preço / 2


def dobro(preço = 0):
    return preço * 2

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')


def resumo(r):
    a = 10
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<20}', end=' ')
    print(f'R${r:.2f}')
    print(f'{"Dobro do preço:":<20}', end=' ')
    print(f'R${dobro(r):.2f:>5}')
    print(f'{"Metade do preço:":<20}', end=' ')
    print(f'R${metade(r):.2f}')
    print(f'{a}% {"de aumento:":<20}', end=' ')
    print(f'R${aumentar(r,a):.2f}')

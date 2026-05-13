from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num = randint(0, 5)
        lista.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO')

def somPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somPar(numeros)




def contagem(ini, fim, passo):
    if passo > 0: x = 1
    else: x = (-1)
    for i in range(ini, fim + x, passo):
        print(f' {i}', end =' ')
        time.sleep(0.5)
    print(f'Fim', end='')

import time
print('='*60)
print('A seguir a sequencia de 1 - 10 ao passo 1')
ini = 0
fim = 10
passo = 1
print('-'*60)
time.sleep(1)
contagem(ini, fim, passo)
time.sleep(1)
print()
print('='*60)
print('Agora a sequencia de 10 - 1 ao passo 2')

ini = 10
fim = 0
passo = -2
print('-'*60)
time.sleep(1)
contagem(ini, fim, passo)
time.sleep(0.7)
print()
print('='*60)
ini = int(input('Qual o valor do inicial? '))
fim = int(input('Qual o valor final? '))
passo = int(input('Qual o passo? '))
print('-='*30)
contagem(ini, fim, passo)
print()
print('-='*30)
print('Programa  Finalizado!!')

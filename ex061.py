primeiro = int(input('Primeiro termo: '))
razao = int(input('Qual sera a razão? '))
limite = 10
limite += 1
contador = 1
pa = 0
print('Os 10 primeiros termos da PA são:')
while not contador == limite:
    print('{} '.format(primeiro), end=' ')
    contador += 1
    primeiro += razao
print('FIM!')
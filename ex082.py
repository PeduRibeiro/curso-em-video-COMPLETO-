pares = list()
impares = list()
total = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    pross = ' '
    while pross not in "NnSs":
        pross = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if pross == 'N':
        break
print('-=' * 30)
print(f'Foram exibidos {len(pares)} pares')
print(f'{pares}')
print('-=' * 30)
print(f'Foram exibidos {len(impares)} impares')
print(f'{impares}')
print('-=' * 30)
print(f'Aqui estão todos os valores: ')
total.extend(pares)
total.extend(impares)
print(f'{total}')
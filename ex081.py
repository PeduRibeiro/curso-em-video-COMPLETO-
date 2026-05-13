valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    print(valores)
    pross = ' '
    while pross not in "NnSs":
        pross = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if pross == 'N':
        break
print('-=' * 30)
print(f'Foram exibidos {len(valores)} valores')
print(f'Essa é a lista de valores em ordem decrescente:\n{sorted(valores)[::-1]}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
print('-=' * 30)
valores = list ()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('\nValor adicionado com sucesso')
    else:
        print('\nValor Duplicado')
    r = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
valores.sort()
print(f'Você digitou os valor{valores}')
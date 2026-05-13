dados = list()
lista = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-'*30)
print(f'Ao todo você cadastrou {len(lista)} pessoa(s).')
print('=-'*30)
print(f'O maior peso foi de {mai} Kg. Peso de:',end= ' ')
for p in lista:
    if p[1] == mai:
        print(f'{p[0]}')
print('=-'*30)
print(f'O menor peso foi de {men} Kg. peso de:',end= ' ')
for p in lista:
    if p[1] == men:
        print(f'{p[0]}')

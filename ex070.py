valortotal = 0
itens1000 = 0
menor = 0
cont = 0
barato = ''
print('=-' * 30)
print('<<<LOJA SUPER BARATÃO>>>')
print('=-' * 30)
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Qual o valor do produto? R$ '))
    cont += 1
    valortotal += preço
    if preço > 1000:
        itens1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip() .upper()
    if continuar == 'N':
        break
print('=-' * 30)
print('{:.^40}'.format(' FIM DO PROGRAMA '))
print(f'O valor total de itens foi R$ {valortotal:.2f}')
print(f'Nessa compra tivemos {itens1000} com valor acima de R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
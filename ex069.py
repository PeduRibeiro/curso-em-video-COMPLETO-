continua = ''
cont = 0
homens = tot18 = totM=0
while True:
    cont += 1
    idade = int(input(f'Qual a idade da {cont}° pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        totM += 1
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua in 'Nn':
        break
    elif continua in 'Ss':
        print('=-' * 30)
        print('{:-^30}'.format('PROXIMO'))
        print('=-' * 30)
print(f'Foram registrados: \n{homens} homen(s)')
print(f'{tot18} pessoa(s) com mais de 18 anos')
print(f'{totM} mulheres com menos de 20 anos')


print('Gerador de PA')
print('-=' *10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Qual sera a razão? '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} '.format(termo), end=' ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você quer mostrar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM!')

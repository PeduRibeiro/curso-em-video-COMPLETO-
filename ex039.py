import datetime
data = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - data
if idade < 18:
    print('Ainda vai se alistar, faltam {} anos para a data'.format(18 - idade))
elif idade == 18:
    print('Hora de se alistar')
else:
    print('Ja passou do tempo de se alistar, ja se passaram {} anos da data'.format(idade - 18))

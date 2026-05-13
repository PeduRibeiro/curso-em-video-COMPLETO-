import datetime
ano = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - ano
if idade < 9:
    print('categoria MIRIM!')
elif idade < 14:
    print('categoria INFANTIL!')
elif idade < 19:
    print('categoria JUNIOR!')
elif idade < 20:
    print('categoria SENIOR!')
else:
    print('categoria MASTER!')
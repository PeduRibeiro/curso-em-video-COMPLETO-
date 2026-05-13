n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('REPROVADO! sua media foi {}...'.format(media))
elif media < 7:
    print('RECUPERAÇÃO! sua media foi {}...'.format(media))
else:
    print('APROVADO! sua media foi {}...'.format(media))

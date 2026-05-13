vel = float(input('A qual a velocidade o carro passou ? '))
if vel >= 80:
    print('Você foi multado no valor de R$ {}'.format((vel - 80)* 7,00))
else:
    print('Velocidade permitida...')


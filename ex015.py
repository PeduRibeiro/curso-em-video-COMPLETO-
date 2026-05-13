dias= float(input('Quantos dias alugados? '))
km= float(input('Quantos km rodados? '))
print('Sabendo que o carro foi alugado por {}dias e percorreu {}km\nO valor do seu aluguel será de: R${}'.format(dias, km, (dias*60)+(km*0.15)))
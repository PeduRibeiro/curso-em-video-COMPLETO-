largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura*altura
print('Sabendo que cada L de tinta cobre uma area equivalente a 2m²... \nPara a sua area de {}, serão utilizados {} L de tinta'.format(area, area/2))
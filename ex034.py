salario1 = float(input('Digite o valor do seu salario: '))
if salario1 > 1250.00:
    print('O salario com aumentto de 10% passara a ser R${:.2f}'.format(salario1*1.10))
else:
    print('O salario com aumento de 15% passara a ser R${:.2f}'.format(salario1*1.15))
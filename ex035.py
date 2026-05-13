A = int(input('Digite a maior reta: '))
B = int(input('Digite o valor da reta 2: '))
C = int(input('Digite o valor da reta 3: '))
if (C + B) <= A:
    print('Sendo {} {} {} os valores das retas NÃO É possivel formar um triangulo'.format(A, B, C))
else:
    print('Sendo {}, {}, {} os valores das retas É SIM possivel formar um triangulo'.format(A, B, C))

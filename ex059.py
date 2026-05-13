n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
botao = 0
while not botao == 5:
    if botao == 1:
        print('\nA soma de {} + {} é: {}'.format(n1,n2,(n1+n2)))
    elif botao == 2:
        print('\nA multiplicação de {} X {} é: {}'.format(n1,n2,(n1*n2)))
    elif botao == 3:
        if n1 > n2:
            print('\nO maior valor é {}\n'.format(n1))
        else:
            print('\nO maior valor é {}'.format(n2))
    elif botao == 4:
        n1 = int(input('\nInforme seu primeiro numero: '))
        n2 = int(input('Informe seu segundo numero: '))
    else:
        print('\nOperação invalida! Tente novamente. ')
    botao= int(input('\nQual a operação desejada:\n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos numeros \n[5] Sair \nOque deseja fazer agora? '))
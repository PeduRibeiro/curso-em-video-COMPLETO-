valor = float(input('Digite o valor do produto: '))
forma = int(input('''selecione a forma de pagamento:
[1] à vista / cheque (10% de desconto)
[2] à vista cartão (5% de desconto)
[3] 2x no cartão
[4] 3x ou mais no cartão
sua opção:  '''))
if forma == 1:
    print('Você ganhou 10% de desconto, valor total R${:.2f}'.format(valor * 0.9))
elif forma == 2:
    print('Você ganhou 5% de desconto, valor total R${:.2f}'.format(valor * 0.95))
elif forma == 3:
    print('Valor da compra R${:.2f}'.format(valor))
else:
    p = int(input('Em quantas vezes você quer parcelar? '))
    print('Valor da compra R${:.2f}'.format(valor*1.2))
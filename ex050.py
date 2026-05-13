soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if (num+1) % 2 != 0:
        soma += num
print('Você informou {} valores e a soma dos PARES informados é {}'.format(cont,soma))
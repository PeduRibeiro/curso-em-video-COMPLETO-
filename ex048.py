soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('O somatorio dos {} valores impares multiplos de 3 foi {} totalizando'.format(cont, soma))
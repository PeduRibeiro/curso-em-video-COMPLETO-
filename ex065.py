lista = list()
num = soma = cont = 0
flag = ''
while not flag == 'N':
    num = int(input('Digite um numero: '))
    flag = str(input('Deseja continuar [S/N]: ')).upper()
    lista.append(int(num))
    soma += num
    cont += 1
    media = (soma) / cont
    maior = max(lista)
    menor = min(lista)
print('A media dos valores digitados é {}'.format(media))
print('Dos valores informados o maior é {}, enquanto o menor é {}'.format(maior, menor))
lista.count(maior)
lista.index(menor)
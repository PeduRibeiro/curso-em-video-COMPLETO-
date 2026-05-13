num = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')
#---------------------------------------------------------
nome = 'Paulo'
idade = 19
salario = 950.50
print(f'O {nome:->20} tem {idade} anos e ganha R${salario:.2f}')
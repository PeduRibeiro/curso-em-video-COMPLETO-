r'''enquanto não maça
    se tiver chão
        passo
    se tiver buraco
        pula
    se tiver moeda
        pega
pega'''
r'''while not maça:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega'''
#-----------------------------------------------------------------------------------------
r'''for c in range(1, 10):
    print(c)
print('fim')'''
r'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('fim')'''
#----------------------------------------------------------------------------------------
r'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim!')'''
#---------------------------------------------------------------------------------------
r'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim!')'''
#-----------------------------------------------------------------------------------------
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} ímpares!'.format(par, impar))

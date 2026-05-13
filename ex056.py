somaidade = 0
mediaidade = 0
maioridadehomem = 0
momevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----{}° PESSOA----'.format(p))
    nome= str(input('Digite o nome: ')).strip()
    idd= int(input('Digite a idade: '))
    sexo= str(input('Digite seu sexo (M/F): ')).strip()
    somaidade += idd
    if p== 1 and sexo in 'Mm':
        maioridadehomem = idd
        nomevelho = nome
    if sexo in 'Mm' and idd > maioridadehomem:
        maioridadehomem = idd
        nomevelho = nome
    if sexo in 'Ff' and idd < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media das idades dessas pessoas é {:.0f}'.format((somaidade)/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
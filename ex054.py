from datetime import date
maior = list()
menor = list()
ano = date.today().year
for c in range(0,7):
    data = int(input('Qual o ano de nascimento da {}° pessoa? '.format(c+1)))
    idade = (ano - data)
    if idade >= 21:
        maior.append(data)
    else:
       menor.append(data)
print('\033[4;34mAo todo tivemos {} maiores de idade...\033[m\n\033[4;31mE tivemos {} menores de idade\033[m'.format(len(maior),len(menor)))
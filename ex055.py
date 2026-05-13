lista = list()
contador = 0
for c in range(0, 5):
    p= float(input('Qual é o peso da {}° pessoa?'.format(c+1)))
    lista.append(float(p))
maior = max(lista)
menor = min(lista)

print('Dos pesos informados o maior é {}Kg. \nEnquanto o menor é {}Kg.'.format(maior, menor))
lista.count(maior)
lista.count(menor)
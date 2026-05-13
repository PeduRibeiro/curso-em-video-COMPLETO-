import moeda


p = float(input('Digite o preço: R$'))
print('-='*23)

print(f'A metade de {(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% de {(p)} temos {moeda.aumentar(p, 10, True)} ')
print(f'Diminuindo 13% de {(p)} temos {moeda.diminuir(p, 13, True)}')
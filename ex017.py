import math
cata = float(input('Digite o cateto adjacente: '))
cato = float(input('Digite o cateto oposto:' ))
hipo = math.hypot(cata, cato)
print('Sendo {}, e {} os catetos do seu triangulo a hipotenusa sera igual a {},'.format(cata, cato, hipo))

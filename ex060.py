#pode ser feito utilizando bibliotecas assim
r'''from math import factorial
num = int(input('Digite um número para \ncalcular o fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))'''
#ou sem bibliotecas assim
num = int(input('Digite um número para calcular o fatorial: '))
c = num
f = 1
print('\nCalculando {}! ...\n'.format(num))
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print('{}'.format(f), end='\n')
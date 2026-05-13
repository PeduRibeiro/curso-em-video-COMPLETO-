a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite mais um numero: '))
d = int(input('Digite um ultimo numero: '))
tupla = (a, b, c, d)
print(f'\nVocê digitou os valores {tupla}')
print(f'\nO numero 9 aparece {tupla.count(9)} vez(es).')
if 3 in tupla:
    print(f'\nO numero 3 aparece pela primeira vez na {tupla.index(3)+1}° posição.\n')
if 3 not in tupla:
    print(f'\nNão existem numeros (3) na listagem\n.')
print('Os numeros pares dessa listagem são:')
if a % 2 == 0:
    print((a), end= ' ')
if b % 2 == 0:
    print((b), end= ' ')
if c % 2 == 0:
    print((c), end= ' ')
if d % 2 == 0:
    print((d), end= ' ')

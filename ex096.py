def area(a, b):
    print('-='* 27)
    print(f'A area de um terreno de {a} x {b} é igual a: {(a * b)}m²')


print('--' *17)
a = float(input('Digite a largura do terreno: '))
b = float(input('Digite o comprimento do terreno: '))

area(a, b)
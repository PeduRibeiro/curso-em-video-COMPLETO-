r'''def titulo(txt):
    print(txt)
    print('-'*30)


#programa principal
titulo('  CURSO EM VIDEO   ')
titulo('  APRENDA PYTHON   ')
titulo('  TALINE LINDA     ')
'''
r'''
def soma(a, b):
    print(f'A soma entre {a} e {b} = {a + b}')
    s = a + b
    print(s)


# Programa principal
soma(a=4,b=5)
soma(b=8,a=9)
soma(2,1)
soma(4,1)
'''
r'''
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
contador(1, 2,  3, 4, 5, 6)
contador( 8 , 0)
contador( 1, 3, 5)
'''
r''''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)
'''
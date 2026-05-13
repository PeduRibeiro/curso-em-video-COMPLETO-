def maior():
    g = max(lista)
    print(f'foram digitados {c} valores, e o maior deles foi {g}')
lista = list()
c = 0
while True:
    num = int(input('digite um valor para incluir a lista [digite 999 para ver o maior]: '))
    if num == 999:
        break
    else:
        lista.append(num)
        c += 1
print('-='*30)
print(lista)
print('-='*30)
maior()
print('Programa Encerrado!!')
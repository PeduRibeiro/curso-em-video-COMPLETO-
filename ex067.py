num = 0
cont = 0
while True:
    cont = 0
    num = int(input(f'Digite um valor para verificar sua tabuada: '))
    print(cont)
    while cont != 10:
        cont += 1
        print('{} x {} = {}'.format(cont, num, num * cont))
    if num < 0:
        break
print('Programa finalizado com sucesso!')

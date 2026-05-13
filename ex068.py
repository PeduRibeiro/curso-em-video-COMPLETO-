from random import randint
cont = -1
escolha1 = ''
print('=-'*30)
print('Vamos jogar PAR ou IMPAR...')
print('=-'*30)
while True:
    while escolha1 not in 'PI':
        escolha1 = str(input('Você escolhe Par (P) ou Impar (I): '))
    print('=-' * 30)
    cont += 1
    maquina = randint(0, 11)
    if escolha1 in 'Pp':
        print(f'Então você é PAR e eu sou IMPAR, vamos la!\n')
    elif escolha1 in 'Ii':
        print(f'Então você é IMPAR e eu sou PAR, vamos la!\n')
    else:
        print('Escolha invalida!')
        break
    jogador = int(input('Qual numero você escolhe? só vale entre 0 e 10 ein!! '))
    print('=-' * 30)
    print(f'Eu escolho {maquina}')
    print(f'Você jogou {jogador} e eu {maquina} a soma deu: {jogador+maquina}.')
    print('=-' * 30)
    if escolha1 in 'Pp':
        if (jogador+maquina) % 2 == 0:
            print('Esse valor é PAR, você venceu!')
            print('=-' * 30)
            print('Vamos jogar NOVAMENTE!')
        else:
            print('Esse valor é IMPAR, você perdeu!')
            break
    if escolha1 in 'Ii':
        if (jogador+maquina) % 2 == 0:
            print('Esse valor é PAR, você perdeu!')
            break
        else:
            print('Esse valor é IMPAR, você venceu!')
            print('=-' * 30)
            print('Vamos jogar NOVAMENTE!')
print('=-'*30)
print(f'Você obteve {cont} vitorias consecutivas:')



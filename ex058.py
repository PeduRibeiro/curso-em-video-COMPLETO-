from random import randint
computador = randint(1,10)
print('Aqui quem fala é seu computador, acabei de pensar em um numero entre 1 e 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print('\nVOCÊ ACERTOU! {} era realmente meu numero! \nUAUU!! Você precisou de {} tentativas para acertar...'.format(computador, palpites))

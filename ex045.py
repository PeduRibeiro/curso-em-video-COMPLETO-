from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
maquina= randint(0,2)
pessoa = int(input('''<<<VAMOS UMA PARTIDA DE JOKENPO>>>
Suas opções são:
[0] PEDRA 
[1] PAPEL
[2] TESOURA
Eai? Qual a sua jogada
'''))
print('-=-' *11)
print('\033[4;31;40mComputador jogou {}\033[m' .format(itens[maquina]))
print('\033[4;36;40mJogador jogou {}\033[m' .format(itens[pessoa]))
print('-=-' *11)
if maquina == 0: # maquina jogou PEDRA
    if pessoa == 0:
        print('\033[1;36;40mEMPATE\033[m')
    elif pessoa == 1:
        print('\033[;30;42mJOGADOR VENCE\033[m')
    elif pessoa == 2:
        print('\033[7;31;40mCOMPUTADOR VENCE!\033[m')
    else:
        print('\033[1;36;40mJOGADA INVALIDA!\033[m')
elif maquina == 1: # maquina jogou PAPEL
    if pessoa == 0:
        print('\033[7;31;40mCOMPUTADOR VENCE!\033[m')
    elif pessoa == 1:
        print('\033[1;36;40mEMPATE\033[m')
    elif pessoa == 2:
        print('\033[;30;42mJOGADOR VENCE\033[m')
    else:
        print('\033[1;36;40mJOGADA INVALIDA!\033[m')

elif maquina == 2: # maquina jogou TESOURA
    if pessoa == 0:
        print("\033[;30;42mJOGADOR VENCE\033[m")
    elif pessoa == 1:
        print('\033[7;31;40mCOMPUTADOR VENCE\033[m')
    elif pessoa == 2:
        print('\033[1;36;40mEMPATE\033[m')
    else:
        print('\033[1;36;40mJOGADA INVALIDA!\033[m')

print('-=-' *11)
print('\033[;36;40mJOGAR NOVAMENTE (crtl + F5)\033[m')
print('-=-' *11)

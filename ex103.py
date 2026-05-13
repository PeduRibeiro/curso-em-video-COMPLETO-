def ficha(jog='<desconecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')


# Programa principal
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '': 
    ficha(gols=gols)
else:
    ficha(nome, gols)

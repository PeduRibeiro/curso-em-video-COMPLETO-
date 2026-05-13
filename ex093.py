parecer = list()
dados = {'nome' : str(input('Qual o nome do atleta: ')),
        'jogos' : int(input(f'Quantas partidas ele jogou: ')),
         'gols' : 0}
marcados = list()
exib = list()
exib.append(dados)
total = 0
for c in range(1, dados['jogos'] + 1):
    ponto = int(input(f'Quantos gols {dados["nome"]} marcou na {c}° partida? '))
    total += ponto
    marcados.append(ponto)
dados ['gols'] = total
parecer.append(dados)
print('-='*30)
print('Lista de gols:')
print(marcados)
print('-='*30)
for e in parecer:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'Então: \nO jogador {dados['nome']} jogou {dados["jogos"]} partidas nesse campeonato.')
for c in range(dados['jogos']):
    print(f'-->Na partida {c+1}, fez {marcados[c]} gols.')
print('-='*30)
print(f'Totalizando assim: {total} gols no campeonato.')
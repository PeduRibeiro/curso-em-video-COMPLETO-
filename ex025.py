nome = str(input('Digite um nome completo: ')).lower().strip()
nome.find('silva')
cond=nome.find(nome.lower('silva'))
if cond == -1:
    print('NÃO')
else:
    print('SIM')
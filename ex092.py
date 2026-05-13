from datetime import date
anoat = date.today().year
lista = list()
ctps = 1
dados = {'nome' : str(input('Digite seu nome: ')),
         'nascimento' : int(input('Digite sua data de nascimento: ')),
         'ctps' : int(input('Digite sua carteira de trabalho (0 se não tem): '))}
dados['idade'] = (anoat - dados['nascimento'])
if not dados['ctps'] == 0:
    compl = {'contratação': int(input('Digite o ano da contratação: ')),
             'salario': float(input('Digite o salario: '))}
    if dados['ctps'] != 0:
        compl['aposentadoria'] = dados['idade'] + ((compl['contratação'] + 35) - date.today().year)
    print('-=' * 30)
    lista.append(dados.copy())
    lista.append(compl.copy())
    for e in lista:
        for k, v in e.items():
            print(f' -{k} tem o valor {v}')
else:
    lista.append(dados.copy())
    for e in lista:
        for k, v in e.items():
            print(f' -{k} tem o valor {v}')
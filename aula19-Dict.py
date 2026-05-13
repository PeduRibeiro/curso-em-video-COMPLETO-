r'''dados = {'nome': 'Pedro', 'idade': 22}
print(dados['nome'])
print(dados.values())
print(dados.keys())
for k,v in dados.items():
    print(f'O {k} é {v}')
'''
#--------------------------------------------------

pessoas = {'nome': 'Paulinho', 'idade': 19, 'amor': 'Taline'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-='*30)
print(pessoas.items())
print('-='*30)
pessoas ['nome'] = 'Taline'
pessoas ['amor'] = 'Paulinho'
pessoas ['idade'] = 25
pessoas ['sexo'] = 'F'
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-='*30)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) 

#---------------------------------------------------
r'''
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''
#---------------------------------------------------------
r'''
estado= dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')
'''
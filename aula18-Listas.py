#listas dentro as listas
r'''pessoas = [['pedro',25], ['Maria', 19], ['João',32]]
dados = list()
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
'''
#-------------------------------------------------------------------
r'''
teste = list()
teste.append('Paulo')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''
#---------------------------------------------------------------------
r'''
galera = [['João', 19],['Ana', 33],['Joaquin', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''
#--------------------------------------------------------------------
galera= list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
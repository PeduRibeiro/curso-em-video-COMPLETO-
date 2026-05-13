r'''tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--FIM--')
'''
 #ou
tempo=int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <=3 else  'carro velho')
print('--FIM--')

#-----------------------------------------------------------------------
nome=str(input('Qual seu primeiro nome?'))
if nome=='paulo':
    print('Bom dia magnata')
else:
    print('Bom dia playboyzinho')
print('Tenha um otimo dia')
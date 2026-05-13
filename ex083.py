conta = list()
A = 0
F = 0
exp = str(input('Digite uma epressão para erificar os parenteses: '))
A = exp.count('(')
F = exp.count(')')
if A == F:
   print('Sua expressão esta correta...')
else:
   print('Sua expressão esta errada...')

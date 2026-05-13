lanche = ('Hamburguer','Suco','Pizza','Pudim')
r'''for comida in lanche:
    print(f'Eu vou comer {comida}')
print('\nComi demais\n')

#------------------------------------------------------------
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
'''
#-----------------------------------------------------------

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição  {pos}')

#-----------------------------------------------------------
print(sorted(lanche))
print(lanche)

a = (2 , 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(2))
print(c)
print(c.index(8))

print( lanche())
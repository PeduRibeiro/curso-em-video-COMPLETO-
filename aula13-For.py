s=0
for c in range(1,3):
    print(c)

i = int(input('Digite um valor para o inicio: '))
f = int(input('Digite um valor para o fim: '))
p = int(input('Digite um valor para o passo: '))
for c in range (i, f+1, p): # 3° numero é iteração (de quantos em quantos)
    print(c)
print('FIM')

for c in range(0,4):
    n= int(input('Digite um valor: '))
    s += n
print('O somatorio de todos os valores foi {}'.format(s))
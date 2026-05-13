import random
numero = int(input("Descubra o número que eu escolhi:"))
num = random.randint(0,5)
if num == numero:
    print('PARABENS VOCÊ ACERTOU!!')
else:
    print('QUE PENA VOCÊ ERROU')
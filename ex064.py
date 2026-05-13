num = contador = soma = 0
fim = 999
while num != 999:
    num = int(input('Digite o numero [999 para parar]: '))
    soma += num
    contador += 1
print('A soma dos numeros é {} e ao todo foram digitado(s) {} numero...'.format(soma-999,contador-1))

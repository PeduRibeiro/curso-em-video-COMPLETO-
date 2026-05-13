numero = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
ordem = int(input('Digite um numero entre 0 e 20: '))
while ordem < 0 or ordem > 20:
    ordem = int(input('Tente novamenteDigite um numero entre 0 e 20: '))
print(f'Você digitou o numero {numero[ordem]}.')
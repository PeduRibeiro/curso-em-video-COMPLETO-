frase = str(input('Digite uma frase: ')).upper() .strip() #.replace(' ', '')
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('\033[34mTemos SIM UM PALINDROMO!\033[m)')
else:
    print('\033[31mA frase NÃO É UM PALINDROMO!\033[m)')
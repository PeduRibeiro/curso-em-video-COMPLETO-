peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso ideal! PARABENS!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30<= imc < 40:
    print('Obesidade!')
else:
    print('Obesidade morbida, CUIDADO!')
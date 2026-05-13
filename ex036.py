casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = float(input('Em quantos anos você quer pagar?'))

mes = anos * 12
parcela = casa / mes

if parcela >= (0.3 * salario):
    print('O seu emprestimo foi aprovado para compra de uma casa no valor de R${:.2f} \n com {:.0f} vezes de R${:.2f}'.format(casa, mes, parcela))
else:
    print('O sua parcela excedeu 30% do seu salario então não podemos liberar o emprestimo')
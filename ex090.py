lista = list()
dados = {'nome': str(input('Nome: '))}
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
if media >= 7:
    dados['situacao'] = 'Aprovado'
if media >= 5 and media <= 7:
    dados['situacao'] = 'Em recuperacao'
if media < 5:
    dados['situacao'] = 'Reprovado'
lista.append(dados.copy())
print('-='*30)
print(f'O aluno(a): {lista[0]['nome']} \nTeve as notas: {nota1:.1f} e {nota2:.1f}...\nAssim sua media final foi {media:.1f} e ele está {lista[0]['situacao']}')
print('-='*30)
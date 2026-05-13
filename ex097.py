def escrever(txt):
    print('~'*(len(txt)+4))
    print(f'  {txt}   ')
    print('~'*(len(txt)+4))


# Programa principal
txt = str(input('Qual titulo deseja escrever? '))
escrever(txt)

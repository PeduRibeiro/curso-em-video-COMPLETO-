valores = list()
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
print(f'O maior valor registrado foi o {max(valores)}, e está na {valores.index(max(valores))+1}ª posição')
print(f'O menor valor registrado foi o {min(valores)}, e está na {valores.index(min(valores))+1}ª posição')
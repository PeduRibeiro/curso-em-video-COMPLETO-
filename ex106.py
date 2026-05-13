def ajuda(com):
    help(com)


#Programa principal
comando =''
while True:
    comando = str(input('Função ou Biblioteca > ')).strip().lower()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
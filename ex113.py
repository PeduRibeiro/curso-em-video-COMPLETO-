def leiaint(msg):
    while True:
        try:
             n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Porfavor digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mErro: O usuario interrompeu o programa.\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Porfavor digite um numero real valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuario interrompeu o programa.\033[m')
            return 0
        else:
            return n

n1 = leiaint('Digite um inteiro: ')
n2 = leiafloat('Digite um real: ')
print(f'O valor iteiro digitado foi {n1} e o valor real foi {n2}')
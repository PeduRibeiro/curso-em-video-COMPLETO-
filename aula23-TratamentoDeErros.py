#tratamentos de erro...

try:
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu n digitar nenhum valor')
except Exception as e:
    print(f'Erro de {e.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
'''
introdução ao try e except
try => tenta executar o código
except => ocorreu algum erro no código
'''

numero_str = input('digite seu número aqui: ')

try:
    print(f'STR: {numero_str}')
    numero_float = float(numero_str)
    print(f'FLOAT: {numero_float}')
    print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')
except:
    print('isso não é um número')


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')
# else:
#     print('isso não é um número')


numero_int = input('Digite um número inteiro: ')

try:
    num_int = int(numero_int)
    if (num_int % 2) == 0:
        print(f'O número que você digitou foi: {num_int} e ele é Par')
    else:
        print(f'O número que você digitou foi: {num_int} e ele é impar')
except:
    print('Isto não é um número inteiro')

horas_usuario = input('digite que horas são em números inteiros: ')
try:
    horas_int = int(horas_usuario)
    if horas_int == 0 or horas_int <= 11:
        print(f'Bom dia, agora são: {horas_int} horas')
    if horas_int >= 12 and horas_int <= 17:
        print(f'Boa tarde agora são: {horas_int} horas')
    if horas_int >= 18 or horas_int == 23:
        print(f'Boa noite, agora são: {horas_int} horas')
except:
    print('isto não é um número em horas, tente novamente... ')

nome_usuário = input('Digite seu nome aqui: ')
quantidade_numeros_nome = len(nome_usuário)

if quantidade_numeros_nome <= 4:
    print(f'seu nome é muito curto, {nome_usuário}')
if quantidade_numeros_nome == 5 or quantidade_numeros_nome == 6:
    print(f'Seu nome é normal, {nome_usuário}')
if quantidade_numeros_nome > 6:
    print(f'Seu nome é muito grande! :D, {nome_usuário}')
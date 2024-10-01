# ==================== Estruturas de Repetições ==================== 

'''
Repetições
=> while (enquanto)

irá repetir o código enquanto a condição for verdadeira
a diferença para o while e para o while True é que o while True é um loop infinito, já que sua condição é sempre verdadeira
e só para quando o laço é quebrado com um break
exemplo:
 while True:
    user_input = input("Digite 'sair' para parar o loop: ")
    if user_input == 'sair':
        break
'''
from time import sleep
while True:
    nome = input('qual seu nome?: ')
    print(f'seu nome é: {nome}')
    
    if nome == 'sair':
        print('saindo....')
        sleep(1)
        break

print('Acabou! :D')



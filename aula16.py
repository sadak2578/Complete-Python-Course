from os import system
from time import sleep



# Primeira parte do código ele pede um comando entrar ou sair
# Além disso utilizo o system para limpar a tela e deixar o terminal organizado
# e utilizo o sleep para deixar as frases em uma ordem mais organizada

sleep(1)
entrada = input('Você quer entrar ou sair?: ')
sleep(1)
system('cls')
sleep(1)

# Aqui eu coloquei um if/else/elif simples, além de ter colocado também um sleep
# Mas não fiz o uso do system
if entrada == 'entrar':
    sleep(1)
    print('bem vindo ao programa :)')
    exit()
# Já aqui eu fiz o uso do system para limpar a tela e o usuário n precisar ficar digitando 'cls' toda vez
# além de fazer o uso do sleep para deixar os textos mais organizados 

elif entrada == 'sair':
    sleep(1)
    print('você saiu do programa... ')
    sleep(3)
    system('cls')
    sleep(1)
    exit()
# aqui é a mesma coisa do anterior
else:
    sleep(1)
    print('você não digitou nem entrar e nem sair...')
    sleep(4)
    system('cls')
    exit()
    
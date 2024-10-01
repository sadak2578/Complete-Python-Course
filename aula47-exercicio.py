from os import system
from time import sleep

palavra_secreta = 'irlanda'
letras_acertadas = ''
numero_tentativas = 0

while True:
    
    
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'palavra formada: {palavra_formada}')
    if palavra_formada == palavra_secreta:
        system('cls')
        print('VOCÊ GANHOU!! PARABÊNS') 
        print(f'A palavra completa era: {palavra_secreta}')
        print(f'O número máximo de tentativas foi: {numero_tentativas}')

        letras_acertadas = ''
        numero_tentativas = 0
        sair = input('Você deseja sair?: [s/n] ').lower().startswith('s')

        if sair is True:
            print('saindo...')
            sleep(5)
            system('cls')
            break
        else:
            print('continuando...')
            sleep(3)
            system('cls')
            continue
        
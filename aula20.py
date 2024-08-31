from os import system
from time import sleep
primeiro_valor = input('Digite o primeiro número: ')
segundo_valor = input('Digite o segundo número: ')
system('cls')
sleep(1)

if primeiro_valor > segundo_valor:

    print(f'primeiro_valor = {primeiro_valor} é maior que segundo_valor = {segundo_valor}')
    sleep(4)
    system('cls')
    exit()
    
elif segundo_valor > primeiro_valor:
    
    print(f'segundo_valor = {segundo_valor} é maior que primeiro_valor = {primeiro_valor}')
    sleep(4)
    system('cls')
    exit()
else: 
    print('ambos os valores são iguais')
    system('cls')
import os
from time import sleep
lista  = []

while True:
    print('====== Selecione uma opção ======')
    opção = input('[i]nserir [a]pagar [l]istar [s]air: ')

    if opção == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opção == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Não há itens para listar')

        for indice, nome in enumerate(lista):
            
            
            print(indice, nome)
    elif opção == 'a':
        indice_str = input('Escolha o índice que vc quer apagar: ')
        os.system('cls') 
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite somente números inteiros')
        except IndexError:
            print('O índice que vc está tentando apagar, não existe na lista, tente novamente')
        except Exception:
            print('erro desconhecido..')
    elif opção == 's':
        print('saindo...')
        sleep(4)
        os.system('cls')
        break
    else:
        print('escolha somente, i, l, s ou a')

        


        
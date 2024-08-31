# ===================== Cálculo de ICM =====================
'''
O calculo de imc é feito de maneira simples, pegamos o peso, e divimos com a altura ao quadrado
em código python ficaria:
imc = peso / (altura) ** 2
'''
from time import sleep
import os 

sleep(1)
print('''
============================================
                    IMC
============================================
''')
sleep(1)
nome = input('Digite seu nome aqui: ')
sleep(1)
altura = float(input('Diogite sua altura: '))
sleep(1)
peso = float(input('Digite seu peso: '))
sleep(1)
imc = peso / (altura ** 2)
sleep(1)
os.system('cls')
sleep(1)
print(f'{nome} tem {altura:.2f} metros de altura')
sleep(1)
print(f'Pesa {peso:.1f}, e seu imc é {imc:.1f}')
sleep(10)
os.system('cls')
exit()

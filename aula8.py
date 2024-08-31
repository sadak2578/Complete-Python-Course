import os
from time import sleep
#Nome, sobrenome, idade, ano de nascimento, é ou não maior de idade, altura em metros

#Primeiro começamos com o nome
sleep(1)
nome = input('Digite seu nome: ')
sleep(1)
#Depois o sobrenome
sleep(1)
sobrenome = input('Digite seu sobrenome: ')
sleep(1)
#Depois a idade
sleep(1)
idade = int(input('Digite sua idade: '))
sleep(1)
#Depois o ano de nascimento
sleep(1)
ano_nascimento = int(input('Digite o ano em que você nasceu: '))
sleep(1)
#Agora se é maior de idade ou não
sleep(1)
maior_idade = idade >= 18
sleep(1)
#depois a altura em metros
sleep(1)
altura = float(input('Digite sua altura aqui: '))
sleep(1)
os.system('cls')
#Por fim printamos tudo na tela
sleep(1)
print(f'Seu nome é: {nome}')
sleep(1)
print(f'Seu sobrenome é: {sobrenome}')
sleep(1)
print(f'Sua idade é: {idade}')
sleep(1)
print(f'você nasceu no ano de:{ano_nascimento}')
sleep(1)
print(f'você é maior de idade?: {maior_idade}')
sleep(1)
print(f'Você tem: {altura} metros de altura')
sleep(10)
#esse 'os.sytem' no final serve para limpar a tela do terminal, para o código ficar mais organizado 
os.system('cls')
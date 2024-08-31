# =========================== Formatação de String com f-string ===========================

'''
Formatação básica de string.

s - string
f - float 
d - int

. <número de dígitos>f
x ou X para Hexadecimal
(caracter) (><^) (quantidade)
> - esquerda
< - direita
^ - centro
= - força o número a aparecer antes do zero
Sinal - + ou -
Ex: 0 > - 10, .1f
conversões de flags - !r, !s, !a 
'''
'''
imaginemos que queiramos fazer um pad, ou seja colocar uma largura fixa em nossa variável:
'''

variavel = 'ABC'
print(f'valor 1: {variavel}')
print(f'valor 2: {variavel : >10}') #isso é um pad, pois eu estou colocando uma largura fixa na minha variável
print(f'valor 3: {variavel : ^10} . ') 
print(f'valor 4: {variavel : <10} . ') 
print(f'{+1000.4584375457298745987439857938:0=+10.1f}')
print(f'o hexadecimal de 1500 é: {1500:08x}')


# ========================== Interpolação ==========================
'''
Interpolação básica de strings 
s - String
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
''' 
nome = 'Luiz'
salário = 100.987
variável = '%s recebe como salário total R$%.2f' % (nome, salário)
print(variável)
print('O hexadecimal de %d é %04x' % (19600, 19600))
